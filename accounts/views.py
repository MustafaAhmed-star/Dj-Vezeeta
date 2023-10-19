from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Profile
from .forms import LoginForm ,UserUpdateForm , UserCreateForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required

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
 


#@login_required(login_url="accounts:login")#  I can do it without (login_url="accounts:login") i can define LOGIN_URL in Settings
@login_required()
def myprofile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'user/myprofile.html',{'profile':profile})  




def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
             
            return redirect('accounts:myprofile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        
    return render(request,'user/update_user.html',{'user_form':user_form})

def signup(request):
    if request.method =='POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print(request.user)
            return redirect('accounts:doctors-list')
    else:
        form = UserCreateForm()
    
    return render(request,'user/signup.html',{'form':form})