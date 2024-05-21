from django.contrib import admin
from django.urls import path
from .views.admin import auth

urlpatterns = [
    path('', auth.index, name='admin-index'),
    path('users/', auth.users),
    path('login/', auth.admin_login, name='admin-login'),
    path('logout/', auth.admin_logout, name='admin-logout'),
    path('company/', auth.company, name='company')
]