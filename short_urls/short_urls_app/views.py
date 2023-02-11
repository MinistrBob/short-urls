from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from .forms import AuthForm
from .models import Link, Click


def home(request):  # HttpRequest
    # Если пользователь не аутентифицирован, то перенаправлять на страницу входа
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app_login'))
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


def links_page(request):
    template = 'links.html'
    context = {
        'user_name': request.user,
        'group_name': 'None'
    }
    return render(request, template, context)


def stat_page(request):
    template = 'stat.html'
    context = {
        'user_name': request.user,
        'group_name': 'None'
    }
    return render(request, template, context)
