from rest_framework.decorators import api_view, permission_classes, authentication_classes
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from .models import AppointmentDiseases,Appointments,Tokens,Payments,Clinics,Diseases,Doctors,Patients,Register
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import TokensSerializer,PaymentsRecordSerializer,AppointmentDiseasesSerializer,AppointmentsSerializer,ClinicsSerializer,PatientsSerializer,DiseasesSerializer,DoctorsSerializer,RegisterSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from django.urls import reverse
import requests
import bcrypt

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def usersignup(request): 
        if request.method == 'POST':
            user=request.data.get('user')
            password=request.data.get('password')
            b_password = password.encode('utf-8')
            django_user, created = User.objects.get_or_create(username=user)               
            if created:
                    django_user.set_password(password) 
                    django_user.save()
            hashed_password = bcrypt.hashpw(b_password, bcrypt.gensalt())
            user_data={
                'username':user,
                'password':hashed_password.decode('utf-8')
            }
            serializer = RegisterSerializer(data=user_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'GET':
            users = Register.objects.all()
            serializer = RegisterSerializer(users, many=True)
            return Response(serializer.data)
        
@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def user_details(request,*awrgs,**kwargs):
        if request.method == 'DELETE':
                pk=kwargs.get('id')
                try:
                    user = Register.objects.get(id=pk).delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
                except Register.DoesNotExist:
                        return Response(status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'GET':
            pk=kwargs.get('id')
            try:
                user = Register.objects.get(id=pk)  
                serializer = RegisterSerializer(user)  
                return Response(serializer.data)
            except Register.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class UserLogin(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(auto_schema=None)
    def post(self, request):
        try:
            user=request.data.get('user')
            password=request.data.get('password')
            users = Register.objects.get(username=user)
            encoded_password=users.password.encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'),encoded_password):
                token_url = reverse('token_obtain_pair')
                token_url = request.build_absolute_uri(token_url)
                payload = {'username': user, 'password': password}
                token_response = requests.post(token_url, json=payload)
                if token_response.status_code == 200:
                    request.session['auth_token'] = token_response.json()['access']
                    return Response({
                        'message': 'Login successful',
                        'token': token_response.json()['access'],
                        'token_refresh': token_response.json()['refresh']
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({'error': f'Invalid credentials token not generated, {token_response.status_code} and {token_response.text}'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({"error": "Invalid password!"}, status=status.HTTP_401_UNAUTHORIZED)
        except Register.DoesNotExist:
            return Response({"error": "User not found!"}, status=status.HTTP_404_NOT_FOUND)    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def token_list(request):
    auth_token = request.session.get('auth_token')
    if not auth_token:
        return Response(
            {"error": "Authentication token not found. Please log in again."},
            status=403
        )
    if request.method == 'GET':
        patients = Tokens.objects.all()
        serializer = TokensSerializer(patients, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TokensSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE','UPDATE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def token_detail(request, id):
    auth_token = request.session.get('auth_token')
    if not auth_token:
        return Response(
            {"error": "Authentication token not found. Please log in again."},
            status=403
        )
    try:
        patient = Tokens.objects.get(id=id)

    except Tokens.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TokensSerializer(patient)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TokensSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'UPDATE':
                patient = Tokens.objects.get(id=id)
                serializer = TokensSerializer(instance=patient, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                return Response(serializer.data)
    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Patient Views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def payment_list(request):
    if request.method == 'GET':
        patients = Payments.objects.all()
        serializer = PaymentsRecordSerializer(patients, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        response['X-Custom-Header'] = 'CustomHeaderValue'
        response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
        return response
    
    elif request.method == 'POST':
        serializer = PaymentsRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_200_OK)
            response['X-Custom-Header'] = 'CustomHeaderValue'
            response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE','UPDATE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def payment_detail(request, id):
    try:
        patient = Payments.objects.get(id=id)

    except Payments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PaymentsRecordSerializer(patient)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        response['X-Custom-Header'] = 'CustomHeaderValue'
        response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
        return response

    elif request.method == 'PUT':
        serializer = PaymentsRecordSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_200_OK)
            response['X-Custom-Header'] = 'CustomHeaderValue'
            response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'UPDATE':
                patient = Payments.objects.get(id=id)
                serializer = PaymentsRecordSerializer(instance=patient, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                response = Response(serializer.data, status=status.HTTP_200_OK)
                response['X-Custom-Header'] = 'CustomHeaderValue'
                response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
                return response
    elif request.method == 'DELETE':
        patient.delete()
        response = Response(serializer.data, status=status.HTTP_200_OK)
        response['X-Custom-Header'] = 'CustomHeaderValue'
        response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
        return response

# Patient Views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def clinic_list(request):
    if request.method == 'GET':
        patients = Clinics.objects.all()
        serializer = ClinicsSerializer(patients, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        response['X-Custom-Header'] = 'CustomHeaderValue'
        response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
        return response

    elif request.method == 'POST':
        serializer = ClinicsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_200_OK)
            response['X-Custom-Header'] = 'CustomHeaderValue'
            response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE','UPDATE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def clinic_detail(request, id):
    try:
        patient = Clinics.objects.get(id=id)

    except Clinics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClinicsSerializer(patient)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        response['X-Custom-Header'] = 'CustomHeaderValue'
        response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
        return response

    elif request.method == 'PUT':
        serializer = ClinicsSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_200_OK)
            response['X-Custom-Header'] = 'CustomHeaderValue'
            response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'UPDATE':
                patient = Clinics.objects.get(id=id)
                serializer = ClinicsSerializer(instance=patient, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    response = Response(serializer.data, status=status.HTTP_200_OK)
                    response['X-Custom-Header'] = 'CustomHeaderValue'
                    response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
                    return response
    elif request.method == 'DELETE':
        patient.delete()
        response = Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        response['X-Custom-Header'] = 'CustomHeaderValue'
        response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
        return response

# Patient Views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def user_list(request):
    if request.method == 'GET':
        patients = Patients.objects.all()
        serializer = PatientsSerializer(patients, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        response['X-Custom-Header'] = 'CustomHeaderValue'
        response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
        return response
    elif request.method == 'POST':
        serializer = PatientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_200_OK)
            response['X-Custom-Header'] = 'CustomHeaderValue'
            response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE','UPDATE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def user_detail(request, id):
    try:
        patient = Patients.objects.get(id=id)

    except Patients.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientsSerializer(patient)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        response['X-Custom-Header'] = 'CustomHeaderValue'
        response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
        return response

    elif request.method == 'PUT':
        serializer = PatientsSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_200_OK)
            response['X-Custom-Header'] = 'CustomHeaderValue'
            response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'UPDATE':
                patient = Patients.objects.get(id=id)
                serializer = PatientsSerializer(instance=patient, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                response = Response(serializer.data, status=status.HTTP_200_OK)
                response['X-Custom-Header'] = 'CustomHeaderValue'
                response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
                return response
    elif request.method == 'DELETE':
        patient.delete()
        response = Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        response['X-Custom-Header'] = 'CustomHeaderValue'
        response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
        return response


# Patient Views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def appointmentdisease_list(request):
    auth_token = request.session.get("auth_token", "")
    request.META['HTTP_AUTHORIZATION'] = f'Bearer {auth_token}'
    if request.method == 'GET':
        patients = AppointmentDiseases.objects.all()
        serializer = AppointmentDiseasesSerializer(patients, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        response['X-Custom-Header'] = 'CustomHeaderValue'
        response['Authorization'] = f'Bearer {auth_token}'
        print("Authorization Token:", auth_token)
        return response
    
    elif request.method == 'POST':
        serializer = AppointmentDiseasesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_200_OK)
            response['X-Custom-Header'] = 'CustomHeaderValue'
            response['Authorization'] = f'Bearer {auth_token}'
            print("Authorization Token:", auth_token)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE','UPDATE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def appointmentdisease_detail(request, id):
    try:
        patient = AppointmentDiseases.objects.get(appointment_id=id)

    except AppointmentDiseases.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentDiseasesSerializer(patient)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AppointmentDiseasesSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'UPDATE':
                patient = AppointmentDiseases.objects.get(id=id)
                serializer = AppointmentDiseasesSerializer(instance=patient, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                return Response(serializer.data)
    elif request.method == 'DELETE':
        patient.delete()
        response = Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        response['X-Custom-Header'] = 'CustomHeaderValue'
        response['Authorization'] = f'Bearer {request.session.get("auth_token", "")}'
        return response
# Doctor Views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def doctor_list(request):
    if request.method == 'GET':
        doctors = Doctors.objects.all()
        serializer = DoctorsSerializer(doctors, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE','UPDATE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def doctor_detail(request, id):
    try:
        doctor = Doctors.objects.get(id=id)
    except Doctors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorsSerializer(doctor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DoctorsSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'UPDATE':
                doctor = Doctors.objects.get(id=id)
                serializer = DoctorsSerializer(instance=doctor, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                return Response(serializer.data)

    elif request.method == 'DELETE':
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Appointment Views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def appointment_list(request):
    if request.method == 'GET':
        appointments = Appointments.objects.all()
        serializer = AppointmentsSerializer(appointments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AppointmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE','UPDATE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def appointment_detail(request, id):
    try:
        appointment = Appointments.objects.get(id=id)
    except Appointments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentsSerializer(appointment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AppointmentsSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'UPDATE':
                appointment = Appointments.objects.get(id=id)
                serializer = AppointmentsSerializer(instance=appointment, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                return Response(serializer.data)

    elif request.method == 'DELETE':
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Medical Record Views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def medicalrecord_list(request):
    if request.method == 'GET':
        medicalrecords = Diseases.objects.all()
        serializer = DiseasesSerializer(medicalrecords, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DiseasesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE','UPDATE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def medicalrecord_detail(request, id):
    try:
        medicalrecord = Diseases.objects.get(id=id)
    except Diseases.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DiseasesSerializer(medicalrecord)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DiseasesSerializer(medicalrecord, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'UPDATE':
                medicalrecord = Diseases.objects.get(id=id)
                serializer = DiseasesSerializer(instance=medicalrecord, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                return Response(serializer.data)
            
    elif request.method == 'DELETE':
        medicalrecord.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
