from django.db import models
from .user import User
from .company import Company
from .job import Job

class Apply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    hr_process = models.IntegerField()
    cover_letter = models.CharField(max_length=2064)
    resume_path = models.CharField(max_length=512)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)