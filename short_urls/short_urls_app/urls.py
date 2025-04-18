from django.urls import path, include
from .views import *
from short_urls_app.views import *
from short_urls_app.utils import not_authorized

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>', redirect_handler, name='redirect_handler'),
    path('app/links-list', LinksList.as_view(), name='links_list'),
    path('app/link/<slug:slug>', LinkEdit.as_view(), name='link_edit'),
    path('app/link-create', LinkCreate.as_view(), name='link_create'),
    path('app/link-del/<slug:slug>', LinkDelete.as_view(), name='link_del'),
    path('app/stat', StatList.as_view(), name='stat'),
    path('app/login', AppLoginView.as_view(), name='login'),
    path('app/logout', AppLogoutView.as_view(), name='logout'),
    path('app/not-authorized', not_authorized, name='not_authorized'),
    path('api/link-create', create_short_link, name='link_create_api'),
]

handler404 = page_not_found_404
handler500 = page_not_found_500
