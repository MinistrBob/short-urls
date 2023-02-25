from django.shortcuts import render
from django.contrib.auth.models import Group


class ContextMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['user_name'] = self.request.user
        context['group_name'] = get_groups(self.request)
        return context


class SuccessMessageMixin:
    """Выводит сообщения об успешных действиях."""

    @property
    def success_message(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


def is_superuser(request):
    """ Проверяет является ли пользователь superuser. """
    if request.user.is_superuser:
        return True
    else:
        return False


def get_groups(request) -> str:
    """Функция проверяет является ли пользователь superuser,
    если нет, тогда возвращает список групп в которых состоит пользователь в виде строки.
    :param request:
    :return: Либо 'superuser' либо список групп (str). """
    if is_superuser(request):
        return 'superuser'
    else:
        query_set = Group.objects.filter(user=request.user)
        if query_set:
            list_group = ''
            for group in query_set:
                list_group += group.name
            return list_group
        else:
            return 'None'


def user_belongs_to_group(request, group_name):
    """Функция проверяет входит ли пользователь в указанную группу."""
    # query_set = Group.objects.filter(user=request.user)
    if request.user.groups.filter(name=group_name).exists():
        return True
    else:
        return False


def not_authorized(request):
    """ Страница для неавторизованных пользователей, которые не включены ни в какую группу,
    поэтому не имеют никаких прав и должны обратиться к администратору.
    :param request:
    :return: """
    template = 'not_authorized.html'
    context = {
        'user_name': request.user,
        'group_name': get_groups(request),
    }
    return render(request, template, context=context)
