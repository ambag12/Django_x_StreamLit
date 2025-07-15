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

## Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- Simple JWT (`djangorestframework-simplejwt`)
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
Signup: POST /api/signup

Login: POST /api/login

Token Protected Routes: Add header Authorization: Bearer <access_token>
## API Endpoints

### Authentication & Users

| Method | Endpoint         | Description           |
|--------|------------------|-----------------------|
| POST   | `/api/signup`    | Register a new user   |
| POST   | `/api/login`     | Obtain JWT tokens     |
| GET    | `/api/user-detail/<id>/` | Retrieve user details |
| DELETE | `/api/user-detail/<id>/` | Delete a user         |

---

### Tokens

| Method | Endpoint                | Description      |
|--------|-------------------------|------------------|
| GET    | `/api/tokenlist/`       | List tokens      |
| POST   | `/api/tokenlist/`       | Create token     |
| GET    | `/api/tokendetail/<id>/`| Retrieve token   |
| PUT    | `/api/tokendetail/<id>/`| Update token     |
| DELETE | `/api/tokendetail/<id>/`| Delete token     |

---

### Payments

| Method | Endpoint                    | Description        |
|--------|-----------------------------|--------------------|
| GET    | `/api/paymentlist/`         | List payments      |
| POST   | `/api/paymentlist/`         | Create payment     |
| GET    | `/api/paymentdetail/<id>/`  | Retrieve payment   |
| PUT    | `/api/paymentdetail/<id>/`  | Update payment     |
| DELETE | `/api/paymentdetail/<id>/`  | Delete payment     |

---

### Clinics

| Method | Endpoint                      | Description        |
|--------|-------------------------------|--------------------|
| GET    | `/api/cliniclist/`            | List clinics       |
| POST   | `/api/cliniclist/`            | Create clinic      |
| GET    | `/api/clinicdetails/<id>/`    | Retrieve clinic    |
| GET    | `/api/clinicdetail/<id>/`     | Duplicate retrieve |
| PUT    | `/api/clinicdetail/<id>/`     | Update clinic      |
| DELETE | `/api/clinicdetail/<id>/`     | Delete clinic      |

---

### Patients

| Method | Endpoint                     | Description         |
|--------|------------------------------|---------------------|
| GET    | `/api/userlist/`             | List patients       |
| POST   | `/api/userlist/`             | Create patient      |
| GET    | `/api/cliniclist/<id>/`      | Retrieve patient    |
| PUT    | `/api/user-detail/<id>/`     | Update patient      |
| DELETE | `/api/user-detail/<id>/`     | Delete patient      |

---

### Appointment-Disease Links

| Method | Endpoint                                  | Description              |
|--------|-------------------------------------------|--------------------------|
| GET    | `/api/appointmentdiseaselist/`            | List appointment-disease |
| POST   | `/api/appointmentdiseaselist/`            | Create link              |
| GET    | `/api/appointmentdiseasedetail/<id>/`     | Retrieve link            |
| PUT    | `/api/appointmentdiseasedetail/<id>/`     | Update link              |
| DELETE | `/api/appointmentdiseasedetail/<id>/`     | Delete link              |

---

### Doctors

| Method | Endpoint                   | Description        |
|--------|----------------------------|--------------------|
| GET    | `/api/doctors/`            | List doctors       |
| POST   | `/api/doctors/`            | Create doctor      |
| GET    | `/api/doctors/<id>/`       | Retrieve doctor    |
| PUT    | `/api/doctors/<id>/`       | Update doctor      |
| DELETE | `/api/doctors/<id>/`       | Delete doctor      |

---

### Appointments

| Method | Endpoint                    | Description         |
|--------|-----------------------------|---------------------|
| GET    | `/api/appointments/`        | List appointments   |
| POST   | `/api/appointments/`        | Create appointment  |
| GET    | `/api/appointments/<id>/`   | Retrieve appointment|
| PUT    | `/api/appointments/<id>/`   | Update appointment  |
| DELETE | `/api/appointments/<id>/`   | Delete appointment  |

---

### Medical Records

| Method | Endpoint                        | Description          |
|--------|---------------------------------|----------------------|
| GET    | `/api/medicalrecords/`          | List records         |
| POST   | `/api/medicalrecords/`          | Create medical record|
| GET    | `/api/medicalrecords/<id>/`     | Retrieve record      |
| PUT    | `/api/medicalrecords/<id>/`     | Update record        |
| DELETE | `/api/medicalrecords/<id>/`     | Delete record        |
