from django.urls import path

from .views import run_worker, run_main

urlpatterns = [
    path('worker/', run_worker, name='run_worker'),
    path('main/', run_main, name='run_main'),
]