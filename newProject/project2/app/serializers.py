from rest_framework import serializers
from .models import AppointmentDiseases,Appointments,Tokens,Payments,Clinics,Diseases,Doctors,Patients,Register


class AppointmentDiseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentDiseases
        fields = '__all__'

class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = '__all__'

class TokensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tokens
        fields = '__all__'

class PaymentsRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
class ClinicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinics
        fields = '__all__'
class DiseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diseases
        fields = '__all__'
class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'
class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
        
