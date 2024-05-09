from django.db import models
from .user import User
from .company import Company

class HrRegister(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)