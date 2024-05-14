from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_nomal_user = models.BooleanField(default=True)

    groups = models.ManyToManyField('auth.Group', related_name='custom_user_set')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_set')