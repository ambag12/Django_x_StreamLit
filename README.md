# Healthcare Appointment API

A Django REST Framework application for managing a healthcare appointment system. Supports user registration, JWT authentication, and CRUD operations for tokens, payments, clinics, patients, appointment-disease links, doctors, appointments, and medical records.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
---
## Features

- **User Management**: Sign up, login, and retrieve user details using Django's `User` model.
- **JWT Authentication**: Secure endpoints with `djangorestframework-simplejwt`.
- **CRUD Operations**: Full create, read, update, delete for:
  - Tokens
  - Payments
  - Clinics
  - Patients
  - Appointment-Disease links
  - Doctors
  - Appointments
  - Medical Records
- **Custom Headers**: Responses include `X-Custom-Header` and `Authorization`.
- **Swagger UI**: API documentation via `drf-yasg`.

## Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- Simple JWT (`djangorestframework-simplejwt`)
- drf-yasg
- bcrypt
- Requests

## Configuration
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate

Create .env 
in .env file:
SECRET_KEY=<your_secret_key>
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

## JWT Settings
in settings.py file:
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
## Running the Application
python manage.py runserver

## Authentication
Signup: POST /usersignup/
{
  "user": "username",
  "password": "pass123"
}
Login: POST /userlogin/
{
  "user": "username",
  "password": "pass123"
}
Returns access and refresh tokens.

Token Refresh: POST /api/token/refresh/
{
  "refresh": "<refresh_token>"
}
Authorization Header:

Authorization: Bearer <access_token>
## API Endpoints
| Method | Endpoint       | Description           |
| ------ | -------------- | --------------------- |
| POST   | `/usersignup/` | Register a new user   |
| GET    | `/usersignup/` | List all users        |
| GET    | `/user/<id>/`  | Retrieve user details |
| DELETE | `/user/<id>/`  | Delete a user         |
| POST   | `/userlogin/`  | Obtain JWT tokens     |
| Method | Endpoint              | Description    |
| ------ | --------------------- | -------------- |
| GET    | `/token_list/`        | List tokens    |
| POST   | `/token_list/`        | Create token   |
| GET    | `/token_detail/<id>/` | Retrieve token |
| PUT    | `/token_detail/<id>/` | Update token   |
| DELETE | `/token_detail/<id>/` | Delete token   |
| Method | Endpoint                | Description      |
| ------ | ----------------------- | ---------------- |
| GET    | `/payment_list/`        | List payments    |
| POST   | `/payment_list/`        | Create payment   |
| GET    | `/payment_detail/<id>/` | Retrieve payment |
| PUT    | `/payment_detail/<id>/` | Update payment   |
| DELETE | `/payment_detail/<id>/` | Delete payment   |
| Method | Endpoint               | Description     |
| ------ | ---------------------- | --------------- |
| GET    | `/clinic_list/`        | List clinics    |
| POST   | `/clinic_list/`        | Create clinic   |
| GET    | `/clinic_detail/<id>/` | Retrieve clinic |
| PUT    | `/clinic_detail/<id>/` | Update clinic   |
| DELETE | `/clinic_detail/<id>/` | Delete clinic   |
| Method | Endpoint             | Description      |
| ------ | -------------------- | ---------------- |
| GET    | `/user_list/`        | List patients    |
| POST   | `/user_list/`        | Create patient   |
| GET    | `/user_detail/<id>/` | Retrieve patient |
| PUT    | `/user_detail/<id>/` | Update patient   |
| DELETE | `/user_detail/<id>/` | Delete patient   |
| Method | Endpoint                           | Description                 |
| ------ | ---------------------------------- | --------------------------- |
| GET    | `/appointmentdisease_list/`        | List links                  |
| POST   | `/appointmentdisease_list/`        | Link disease to appointment |
| GET    | `/appointmentdisease_detail/<id>/` | Retrieve link               |
| PUT    | `/appointmentdisease_detail/<id>/` | Update link                 |
| DELETE | `/appointmentdisease_detail/<id>/` | Remove link                 |
| Method | Endpoint               | Description     |
| ------ | ---------------------- | --------------- |
| GET    | `/doctor_list/`        | List doctors    |
| POST   | `/doctor_list/`        | Create doctor   |
| GET    | `/doctor_detail/<id>/` | Retrieve doctor |
| PUT    | `/doctor_detail/<id>/` | Update doctor   |
| DELETE | `/doctor_detail/<id>/` | Delete doctor   |
| Method | Endpoint                    | Description          |
| ------ | --------------------------- | -------------------- |
| GET    | `/appointment_list/`        | List appointments    |
| POST   | `/appointment_list/`        | Create appointment   |
| GET    | `/appointment_detail/<id>/` | Retrieve appointment |
| PUT    | `/appointment_detail/<id>/` | Update appointment   |
| DELETE | `/appointment_detail/<id>/` | Delete appointment   |
| Method | Endpoint                      | Description          |
| ------ | ----------------------------- | -------------------- |
| GET    | `/medicalrecord_list/`        | List medical records |
| POST   | `/medicalrecord_list/`        | Create record        |
| GET    | `/medicalrecord_detail/<id>/` | Retrieve record      |
| PUT    | `/medicalrecord_detail/<id>/` | Update record        |
| DELETE | `/medicalrecord_detail/<id>/` | Delete record        |
