from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('doctors/',views.doctors_list ,name='doctors-list'),
    path('login/',views.user_login ,name='login'),
    path('signup/',views.signup ,name='signup'),
    path('myprofile/',views.myprofile ,name='myprofile'),
    path('user/update',views.user_update ,name='user-update'),
    path('myprofile/update/',views.update_profile ,name='profile-update'),
    path('doctors/<str:slug>/',views.doctor_detail ,name='doctor-detail'),
]