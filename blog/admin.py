from django.contrib import admin
from .models import UserModel, Appointment, ClinicModel

admin.site.register(UserModel)
admin.site.register(Appointment)
admin.site.register(ClinicModel)
