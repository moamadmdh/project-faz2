from django.db import models
from .validators import *
   
class User(models.Model):
    user_type = models.CharField(max_length=10, choices=[('patient', 'Patient'), ('secretary', 'Secretary')], default='patient'
    )
    username = models.CharField(max_length = 20, unique = True, validators = [username_validators]
    )
    password = models.CharField(max_length = 50, unique = False, validators = [password_validators]
    )
    email = models.EmailField(max_length = 254, blank = True, null = True
    )
    
class ClinicModel(models.Model):
    clinic_id = models.CharField(max_length=255, unique=True
    )
    name = models.CharField(max_length=255
    )
    address = models.CharField(max_length=255
    )
    contact_info = models.CharField(max_length=255, unique=True
    )
    services = models.CharField(max_length=255,null=True
    )
import uuid   
class Appointment(models.Model):
    appointmentID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    clinic_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    dateTime = models.DateField(max_length=255)
    status = models.CharField(max_length=20)
