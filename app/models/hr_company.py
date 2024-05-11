from django.db import models
from .hr_register import HrRegister
from .company import Company

class HRCompany(models.Model):
    hr = models.ForeignKey(HrRegister, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)