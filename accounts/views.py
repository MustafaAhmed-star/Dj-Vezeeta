from django.shortcuts import render
#from django.contrib.auth.models import User
from .models import Profile
# Create your views here.
def doctors_list(request):
    doctors = Profile.objects.all()
    context ={
        'doctors':doctors
    }
    return render(request,'user/doctors_list.html',context=context)