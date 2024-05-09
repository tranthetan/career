from django.db import models

class User(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    status = models.BooleanField(default=True)
    password = models.CharField(max_length=255)
    role_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)