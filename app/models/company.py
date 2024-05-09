from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField()
    address = models.TextField()
    thumbnail = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)