from django.contrib import admin
from .models import AppointmentDiseases,Appointments,Tokens,Payments,Clinics,Diseases,Doctors,Patients
# Register your models here.
admin.site.register(AppointmentDiseases)
admin.site.register(Appointments)
admin.site.register(Tokens)
admin.site.register(Clinics)
admin.site.register(Diseases)
admin.site.register(Doctors)
admin.site.register(Patients)
admin.site.register(Payments)

