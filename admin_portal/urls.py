from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='admin-index'),
    path('users/', users),
    path('login/', admin_login, name='admin-login'),
    path('logout/', admin_logout, name='admin-logout')
]