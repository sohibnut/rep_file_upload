# core/urls.py
from django.urls import path
from .views import download_by_code

urlpatterns = [
    path('<slug:code>/', download_by_code),
]
