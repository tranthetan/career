from django.contrib import admin
from django.urls import path
from .views import index, auth, user, job

urlpatterns = [
    path('', index.index, name='home'),
    path('login', auth.index, name='login'),
    path('register', user.register_form),
    path('job/<int:job_id>/detail', job.show),
    path('job/search', index.search, name='job-search'),
    path('user/register', user.register_view, name='user-register'),
    path('user/login', auth.login_view, name='user-login'),
    path('user/logout', auth.logout_view, name='user-logout'),
]