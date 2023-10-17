from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Profile
from .forms import LoginForm
from django.contrib.auth import login,authenticate
# Create your views here.
def doctors_list(request):
    doctors = Profile.objects.all()
    context ={
        'doctors':doctors
    }
    return render(request,'user/doctors_list.html',context=context)


def doctor_detail(request,slug):
    doctor_detail = Profile.objects.get(slug=slug)
    context ={
        'doctor_detail':doctor_detail
    }
    return render(request,'user/doctor_details.html',context=context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:doctors-list')
    else:
        form = LoginForm()
    return render(request,'user/login.html',{'form':form})
 



def myprofile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'user/myprofile.html',{'profile':profile})  