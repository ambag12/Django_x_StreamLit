# Healthcare Appointment API


This project is a Django REST Framework (DRF) application that provides a comprehensive API for managing a healthcare appointment system. It supports user registration, authentication, and CRUD operations for tokens, payments, clinics, patients, appointment diseases, doctors, appointments, and medical records.

Table of Contents

Features

Tech Stack

Installation

Configuration

Running the Application

Authentication

API Endpoints

User Signup & Login

Tokens

Payments

Clinics

Patients

Appointment Diseases

Doctors

Appointments

Medical Records

Serializers & Models

Swagger Documentation

Contributing

License

Features

User Management: Sign up, login, and user details with Django User model integration

JWT Authentication: Secured endpoints using djangorestframework-simplejwt

CRUD Operations: Full create, read, update, delete functionality for tokens, payments, clinics, patients, appointment diseases, doctors, appointments, and medical records

Custom Headers: Responses include custom headers such as X-Custom-Header and Authorization

Swagger UI: Integrated with drf-yasg for API documentation

Tech Stack

Python 3.x

Django 4.x

Django REST Framework

Simple JWT (djangorestframework-simplejwt)

drf-yasg

bcrypt

Requests

Installation

Clone the repository

git clone <repository_url>
cd <project_directory>

Create a virtual environment

python3 -m venv venv
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Apply migrations

python manage.py migrate

Create a superuser (optional)

python manage.py createsuperuser

Configuration

Environment Variables: Create a .env file (or use Django settings) with the following keys:

SECRET_KEY=<your_secret_key>
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

JWT Settings: In settings.py, configure Simple JWT:

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

Running the Application

python manage.py runserver

Visit http://127.0.0.1:8000/ to view the API and http://127.0.0.1:8000/swagger/ for Swagger UI.

Authentication

Signup: POST /usersignup/ with user and password fields

Login: POST /userlogin/ with user and password to receive access and refresh tokens

Token Refresh: Use the refresh endpoint provided by Simple JWT (/api/token/refresh/)

Include the Authorization: Bearer <access_token> header in subsequent requests.

API Endpoints

User Signup & Login

Method

Endpoint

Description

POST

/usersignup/

Register a new user

GET

/usersignup/

List all registered users

DELETE

/user/<id>/

Delete a user (authenticated)

GET

/user/<id>/

Get user details (authenticated)

POST

/userlogin/

Login and obtain JWT tokens

Tokens

Method

Endpoint

Description

GET

/token_list/

List all tokens

POST

/token_list/

Create a new token

GET

/token_detail/<id>

Retrieve token details

PUT

/token_detail/<id>

Update a token

DELETE

/token_detail/<id>

Delete a token

Payments

Method

Endpoint

Description

GET

/payment_list/

List all payments

POST

/payment_list/

Create a payment record

GET

/payment_detail/<id>

Retrieve a payment record

PUT

/payment_detail/<id>

Update a payment record

DELETE

/payment_detail/<id>

Delete a payment record

Clinics

Method

Endpoint

Description

GET

/clinic_list/

List clinics

POST

/clinic_list/

Create clinic

GET

/clinic_detail/<id>

Retrieve clinic detail

PUT

/clinic_detail/<id>

Update clinic

DELETE

/clinic_detail/<id>

Delete clinic

Patients

Method

Endpoint

Description

GET

/user_list/

List patients

POST

/user_list/

Create patient

GET

/user_detail/<id>

Retrieve patient detail

PUT

/user_detail/<id>

Update patient

DELETE

/user_detail/<id>

Delete patient

Appointment Diseases

Method

Endpoint

Description

GET

/appointmentdisease_list/

List appointment-disease links

POST

/appointmentdisease_list/

Link disease to appointment

GET

/appointmentdisease_detail/<id>

Get diseases for an appointment

PUT

/appointmentdisease_detail/<id>

Update appointment-disease link

DELETE

/appointmentdisease_detail/<id>

Remove disease link

Doctors

Method

Endpoint

Description

GET

/doctor_list/

List doctors

POST

/doctor_list/

Create doctor

GET

/doctor_detail/<id>

Retrieve doctor detail

PUT

/doctor_detail/<id>

Update doctor

DELETE

/doctor_detail/<id>

Delete doctor

Appointments

Method

Endpoint

Description

GET

/appointment_list/

List appointments

POST

/appointment_list/

Create appointment

GET

/appointment_detail/<id>

Get appointment detail

PUT

/appointment_detail/<id>

Update appointment

DELETE

/appointment_detail/<id>

Delete appointment

Medical Records

Method

Endpoint

Description

GET

/medicalrecord_list/

List medical records

POST

/medicalrecord_list/

Create medical record

GET

/medicalrecord_detail/<id>

Get medical record

PUT

/medicalrecord_detail/<id>

Update medical record

DELETE

/medicalrecord_detail/<id>

Delete medical record

Serializers & Models

Models: AppointmentDiseases, Appointments, Tokens, Payments, Clinics, Diseases, Doctors, Patients, Register

Serializers: TokensSerializer, PaymentsRecordSerializer, AppointmentDiseasesSerializer, AppointmentsSerializer, ClinicsSerializer, PatientsSerializer, DiseasesSerializer, DoctorsSerializer, RegisterSerializer

Each serializer maps directly to its corresponding model for seamless validation and serialization.
