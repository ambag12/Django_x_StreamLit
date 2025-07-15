# Healthcare Appointment API

A Django REST Framework application for managing a healthcare appointment system. Supports user registration, JWT authentication, and CRUD operations for tokens, payments, clinics, patients, appointment-disease links, doctors, appointments, and medical records.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
  - [User Signup & Login](#user-signup--login)
  - [Tokens](#tokens)
  - [Payments](#payments)
  - [Clinics](#clinics)
  - [Patients](#patients)
  - [Appointment Diseases](#appointment-diseases)
  - [Doctors](#doctors)
  - [Appointments](#appointments)
  - [Medical Records](#medical-records)
- [Serializers & Models](#serializers--models)
- [Swagger Documentation](#swagger-documentation)
- [Contributing](#contributing)
- [License](#license)

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

