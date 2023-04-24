# TODO: Не нужно кнопку, нужно просто форму создания возвращать сразу с проставленным слагом, если человек хочет, то может удалить его и поставить свой. Сделать кнопку генерации слага - слаг нужно проверять на уникальность.
# TODO: Добавить в Link creater, editor (те кто создал ссылку и последний редактор). https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-editing/#models-and-request-user
# TODO: Добавить шаблоны ссылок.
# TODO: Имя и группа отображаются не на всех страницах.
# TODO: При заходе на s.gs.org перебрасывать на основной сайт школы.   /app/home
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.utils.crypto import get_random_string
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import *
from .utils import get_groups
from .models import Link, Click
from django.contrib.auth.mixins import LoginRequiredMixin

SLUG_CHARS = "abcdefghijklmnopqrstuvwxyz0123456789-_"


def get_slug():
    return get_random_string(6, SLUG_CHARS)


def home(request):  # HttpRequest
    # Если пользователь не аутентифицирован, то перенаправлять на страницу входа
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    # На работу в приложении имеют права: суперпользователь и члены группы managers
    if request.user.is_superuser or request.user.groups.filter(name='managers').exists():
        template = 'index.html'
        context = {
            'user_name': request.user,
            'group_name': get_groups(request),
        }
        return render(request, template, context)
    # иначе все остальные (пользователи без группы не имеют прав и должны обратиться к администратору)
    else:
        return HttpResponseRedirect(reverse('not_authorized'))


def redirect_handler(request, slug):
    try:
        link = Link.objects.get(short_url=slug, is_enabled=True)
        ip = get_client_ip(request)
        user_agent = request.META["HTTP_USER_AGENT"]
        print(f"Client-IP: {ip}")
        print(f"User-agent: {user_agent}")
        click = Click(link=link, ip=ip, user_agent=user_agent)
        click.save()
        return redirect(link.long_url, permanent=True)
        # return HttpResponse(f"<h1>Redirect from {slug}</h1>")
    except Link.DoesNotExist:
        raise Http404()
    # if slug == 'main':
    #     return redirect('https://en.givinschool.org/', permanent=True)
    #     # return HttpResponse(f"<h1>Redirect from {slug}</h1>")
    # else:
    #     raise Http404()


def page_not_found_404(request, exception):
    return HttpResponseNotFound(f"<h1>You either have the wrong URL or it is disabled.<br>"
                                f"Make sure you enter the URL correctly or "
                                f"ask whoever gave you the URL to give you the correct one.</h1>")


def page_not_found_500(request):
    return HttpResponseNotFound(f"<h1>ERROR 500</h1>")


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AppLoginView(LoginView):
    """ Страница Login. """
    template_name = 'app_login.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url


class AppLogoutView(LogoutView):
    """ Logout - перенаправление на главную страницу. """
    next_page = reverse_lazy('login')


class LinksList(LoginRequiredMixin, ListView):
    model = Link
    template_name = 'links_list.html'
    context_object_name = 'links'
    paginate_by = 30
    login_url = '/app/login'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        context['user_name'] = self.request.user
        context['group_name'] = get_groups(self.request)
        return context

    def get_queryset(self):
        # return Link.objects.filter(is_enabled=True)
        return Link.objects.all().order_by('-time_update')


class LinkCreate(CreateView):
    form_class = AddLinkForm
    template_name = 'link_create.html'
    success_url = reverse_lazy('links_list')

    # def post(self, request):
    #     print(request.POST)
    #     return HttpResponse('Thank you for your message!')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_name'] = self.request.user
        context['group_name'] = get_groups(self.request)
        return context

    def get_initial(self):
        init_data = {'short_url': get_slug()}
        return init_data


class LinkEdit(UpdateView):
    model = Link
    template_name = 'links_list.html'
    form_class = EditLinkForm
    success_url = reverse_lazy('links_list')
    success_message = "Коротка ссылка изменена"
    slug_field = 'short_url'

    def get_context_data(self, **kwargs):
        kwargs['edit'] = True
        context = super().get_context_data(**kwargs)
        context['user_name'] = self.request.user
        context['group_name'] = get_groups(self.request)
        return context

    def form_valid(self, form_class):
        return super(LinkEdit, self).form_valid(form_class)


class LinkDelete(DeleteView):
    """ (Класс DeleteView в отличие от функции работает методом POST!!!) """
    model = Link
    template_name = 'link_delete.html'
    success_url = reverse_lazy('links_list')
    success_message = "Короткая ссылка удалена"
    slug_field = 'short_url'

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().post(request)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_name'] = self.request.user
        context['group_name'] = get_groups(self.request)
        return context


class StatList(LoginRequiredMixin, ListView):
    model = Click
    template_name = 'stat.html'
    context_object_name = 'stats'
    paginate_by = 50
    login_url = '/app/login'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_name'] = self.request.user
        context['group_name'] = get_groups(self.request)
        return context
