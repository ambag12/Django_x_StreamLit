from django.urls import path
from . import views 
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/login', views.UserLogin.as_view(), name='login'),
    path('api/user-detail/<int:id>/', views.user_details, name='user_details'),
    path('api/signup',views.usersignup, name='signup-details'),
    path('api/appointmentdiseaselist/', views.appointmentdisease_list, name='appointmentdisease_list'),
    path('api/appointmentdiseasedetail/<int:id>/', views.appointmentdisease_detail, name='appointmentdisease_list'),
    path('api/doctors/', views.doctor_list, name='doctor-list'),
    path('api/doctors/<int:id>/', views.doctor_detail, name='doctor-detail'),
    path('api/appointments/', views.appointment_list, name='appointment-list'),
    path('api/appointments/<int:id>/', views.appointment_detail, name='appointment-detail'),
    path('api/medicalrecords/', views.medicalrecord_list, name='medicalrecord-list'),
    path('api/medicalrecords/<int:id>/', views.medicalrecord_detail, name='medicalrecord-detail'),
    path('api/clinicdetails/<int:id>/', views.clinic_detail, name='clinic-detail'),
path('api/cliniclist/', views.clinic_list, name='clinic-list'),
path('api/tokendetail/<int:id>/', views.token_detail, name='token-detail'),
path('api/tokenlist/', views.token_list, name='token-list'),
path('api/paymentdetail/<int:id>/', views.payment_detail, name='payment-detail'),
path('api/paymentlist/', views.payment_list, name='payment-list'),
path('api/clinicdetail/<int:id>/', views.clinic_detail, name='clinic-detail'),
path('api/userlist/', views.user_list, name='user-list'),
path('api/cliniclist/<int:id>/', views.user_detail, name='user-detail'),

]
