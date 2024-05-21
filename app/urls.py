from django.contrib import admin
from django.urls import path
from .views import index, auth, user, job

urlpatterns = [
    path('', index.index, name='home'),
    path('login', auth.index),
    path('register', user.register),
    path('job/<int:job_id>/detail', job.show),
    path('job/search', index.search, name='job-search'),
]