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


def get_group(request):
    """ Проверяет является ли пользователь superuser, тогда ему всё разрешено, или в каких группах состоит пользователь.
    :param request:
    :return: Либо 'superuser' либо список групп. """
    if is_superuser(request):
        return 'superuser'
    else:
        query_set = Group.objects.filter(user=request.user)
        list_group = ''
        for group in query_set:
            list_group += group.name
        return list_group


def user_belongs_to_group(request, group_name):
    """ Проверяет входит ли пользователь в группу. """
    # query_set = Group.objects.filter(user=request.user)
    if request.user.groups.filter(name=group_name).exists():
        return True
    else:
        return False


def not_authorized(request):
    """ Страница для неавторизованных пользователей, которые не включены ни в какую группу,
    поэтому не имеют гикаких прав и должны обратиться к администратору.
    :param request:
    :return: """
    template = 'not_authorized.html'
    context = {
        'user_name': 'None',
        'group_name': 'None'
    }
    return render(request, template, context=context)
