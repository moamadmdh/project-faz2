from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('M', 'منشی'),
        ('P', 'بیمار'),
    )
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)
  
