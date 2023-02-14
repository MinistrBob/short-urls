# TODO: Login\Logout
# TODO: В readme.md ошибка при входе пользователя demo он получается как неавторизованный пользователь.
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.utils.crypto import get_random_string
from .forms import *
from .models import Link, Click


def home(request):  # HttpRequest
    # Если пользователь не аутентифицирован, то перенаправлять на страницу входа
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    # суперпользователь, то ему можно всё и показывать всё
    if request.user.is_superuser:
        template = 'index.html'
        context = {
            'user_name': request.user,
            'group_name': 'None'
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
    form_class = AuthForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url


class AppLogoutView(LogoutView):
    """ Logout - перенаправление на главную страницу. """
    next_page = reverse_lazy('home')


def links_list(request):
    # links = Link.objects.all()
    links = Link.objects.filter(is_enabled=True)
    template = 'links_list.html'
    context = {
        'request': request,
        'links': links,
    }
    return render(request, template, context)


def stat_page(request):
    stats = Click.objects.all()
    template = 'stat.html'
    context = {
        'user_name': request.user,
        'group_name': 'None',
        'stats': stats
    }
    return render(request, template, context)


def link_edit(request, link_id):
    link = get_object_or_404(Link, short_url=link_id)
    context = {
        'link': link,
    }
    return render(request, 'link_edit.html', context=context)


def link_create(request):
    if request.method == 'POST':
        form = AddLinkForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                Link.objects.create(**form.cleaned_data)
                return redirect('links_list')
            except:
                form.add_error(None, 'Ошибка создания короткой ссылки. Возможно что такая короткая ссылка уже есть.')
    else:
        form = AddLinkForm()
    return render(request, 'link_create.html', {'form': form})


def link_del(request, link_id):
    link = get_object_or_404(Link, pk=link_id)
    link.delete()
    return redirect('links_list')


# how to autorize only manager group users and superuser
def login(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = AuthForm()
    return render(request, 'login.html', {'form': form})