from django.db import models
from .user import User
from .company import Company
from .career import Career

class WorkType(models.Model):
    name = models.CharField(max_length=255)
    work_from = models.CharField(max_length=15)
    work_to = models.CharField(max_length=15)
