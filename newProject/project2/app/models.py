from django.contrib.auth.models import AbstractUser
from django.db import models

class AppointmentDiseases(models.Model):
    appointment = models.OneToOneField('Appointments', models.DO_NOTHING) 
    disease = models.ForeignKey('Diseases', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'appointment_diseases'


class Appointments(models.Model):
    patient = models.ForeignKey('Patients', models.DO_NOTHING)
    doctor = models.ForeignKey('Doctors', models.DO_NOTHING)
    clinic = models.ForeignKey('Clinics', models.DO_NOTHING,blank=True, null=True)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'appointments'


class Clinics(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'clinics'


class Diseases(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'diseases'


class Doctors(models.Model):
    username = models.ForeignKey('Patients', models.DO_NOTHING)
    clinic = models.ForeignKey(Clinics, models.DO_NOTHING,blank=True, null=True)
    specialization = models.CharField(max_length=100,blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'doctors'


class Payments(models.Model):
    appointment = models.ForeignKey(Appointments, models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'payments'


class Tokens(models.Model):
    appointment = models.ForeignKey(Appointments, models.DO_NOTHING)
    token_number = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tokens'


class Patients(models.Model):
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=100,blank=True, null=True)
    phone_number = models.CharField(max_length=15,blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users'

class Register(models.Model):
    phone_number = models.CharField(max_length=15,blank=True, null=True)
    username=models.CharField(unique=True, max_length=50)
    password =models.TextField(max_length=300,null=False,blank=False)
    user_type = models.CharField(max_length=10,blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    logged_in = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'register'
