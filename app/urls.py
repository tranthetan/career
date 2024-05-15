from django.contrib import admin
from django.urls import path
from .views import index, auth

urlpatterns = [
    path('', index.index),
    path('login', auth.index),
]