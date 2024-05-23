from django.contrib import admin
from django.urls import path
from .views.admin import auth
from .views.admin import user

urlpatterns = [
    path('', auth.index, name='admin-index'),
    path('users-hr/', user.users_hr, name='users-hr'),
    path('users-normal/', user.users_normal, name='users-normal'),
    path('toggle-user-active/<int:user_id>/', user.toggle_user_active, name='toggle_user_active'),
    path('login/', auth.admin_login, name='admin-login'),
    path('logout/', auth.admin_logout, name='admin-logout'),
    path('company/', auth.company, name='admin-company')
]