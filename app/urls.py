from django.contrib import admin
from django.urls import path
from .views import index, auth, user

urlpatterns = [
    path('', index.index),
    path('login', auth.index),
    path('filter', auth.index),
    path('register', user.register),
]