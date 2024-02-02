from django.contrib import admin
from .models import User, Appointment, ClinicModel

admin.site.register(User)
admin.site.register(Appointment)
admin.site.register(ClinicModel)
