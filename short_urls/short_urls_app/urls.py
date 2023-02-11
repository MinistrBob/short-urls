from django.urls import path, include
from .views import *
from short_urls_app.views import *
from short_urls_app.utils import not_authorized

urlpatterns = [
    path('', home, name='home'),
    path('app/links', links_page, name='links'),
    path('app/stat', stat_page, name='stat'),
    path('<slug:slug>', redirect_handler, name='redirect_handler'),
    path('app/login', AppLoginView.as_view(), name='login'),
    path('app/logout', AppLogoutView.as_view(), name='logout'),
    path('app/not-authorized', not_authorized, name='not_authorized'),
]

handler404 = page_not_found_404
handler500 = page_not_found_500
