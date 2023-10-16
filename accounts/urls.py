from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('doctors/',views.doctors_list ,name='doctors-list'),
    path('doctors/login',views.user_login ,name='login'),
    path('doctors/<str:slug>/',views.doctor_detail ,name='doctor-detail'),
]