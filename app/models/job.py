from django.db import models
from .user import User
from .company import Company
from .career import Career
from .work_type import WorkType

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary_range = models.CharField(max_length=255)
    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, related_name='job_creations', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    level = models.CharField(max_length=30)
    count_apply = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)