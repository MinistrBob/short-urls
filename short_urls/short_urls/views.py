from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound
from django.shortcuts import redirect


def home(request):  # HttpRequest
    return HttpResponse("<h1>Home page</h1>")


def redirect_handler(request, slug):
    if slug == 'main':
        return redirect('https://en.givinschool.org/', permanent=True)
        # return HttpResponse(f"<h1>Redirect from {slug}</h1>")
    else:
        raise Http404()


def page_not_found_404(request, exception):
    return HttpResponseNotFound(f"<h1>ERROR 404</h1>")


def page_not_found_500(request):
    return HttpResponseNotFound(f"<h1>ERROR 500</h1>")