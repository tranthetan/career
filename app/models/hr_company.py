from django.db import models
from .user import User
from .company import Company

class HRCompany(models.Model):
    hr = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)