# core/urls.py
from django.urls import path
from .views import download_by_code, main

urlpatterns = [
    path('<slug:code>/', download_by_code),
    path('', main, name='main'),
]
