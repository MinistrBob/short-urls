from django.urls import path, include
from .views import *
from short_urls_app.views import *
from short_urls_app.utils import not_authorized

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>', redirect_handler, name='redirect_handler'),
    path('app/links-list', links_list, name='links_list'),
    path('app/link/<slug:link_id>', link_edit, name='link_edit'),
    path('app/link-create', link_create, name='link_create'),
    path('app/link-del/<slug:link_id>', link_del, name='link_del'),
    path('app/stat', stat_page, name='stat'),
    path('app/login', AppLoginView.as_view(), name='login'),
    path('app/logout', AppLogoutView.as_view(), name='logout'),
    path('app/not-authorized', not_authorized, name='not_authorized'),
]

handler404 = page_not_found_404
handler500 = page_not_found_500
