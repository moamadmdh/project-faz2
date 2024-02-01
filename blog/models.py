from django.db import models
from .validators import *


class Patient(models.Model):
    user_type = models.CharField(
        max_length=10,
        choices=[('patient', 'Patient'), ('secretary', 'Secretary')],
        default='patient'
    )
    username = models.CharField(
            max_length = 20,
            unique = True,
            validators = [username_validators]
        )
    password = models.CharField(
            max_length = 50,
            unique = False,
            validators = [password_validators]
        )
    email = models.EmailField(
            max_length = 254,
            blank = True,
            null = True
        )
   
   
class Secretary(models.Model):
    user_type = models.CharField(
        max_length=10,
        choices=[('patient', 'Patient'), ('secretary', 'Secretary')],
        default='patient'
    )
    username = models.CharField(
            max_length = 20,
            unique = True,
            validators = [username_validators]
        )
    password = models.CharField(
            max_length = 50,
            unique = False,
            validators = [password_validators]
        )
    email = models.EmailField(
            max_length = 254,
            blank = True,
            null = True
        )
