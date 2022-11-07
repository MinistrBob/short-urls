from django.urls import path, include
from .views import home, redirect_handler, page_not_found_404, page_not_found_500

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>', redirect_handler, name='redirect_handler'),
]

handler404 = page_not_found_404
handler500 = page_not_found_500
