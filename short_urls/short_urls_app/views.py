from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound
from django.shortcuts import redirect
from .models import Link, Click


def home(request):  # HttpRequest
    return HttpResponse(f"<h1>Home page</h1>")


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
