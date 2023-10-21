from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, ProfilePatient



class UserCreateForm(UserCreationForm):
    username = forms.CharField(label='اسم المستخدم')    
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الثاني')
    email = forms.EmailField(label='البريد الالكتروني')
    password1 = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput,min_length=8)
    password2 = forms.CharField(label='تاكيد كلمة المرور', widget=forms.PasswordInput,min_length=8)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email','password1','password2')

class LoginForm(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم')
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']



class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الثاني')
    email = forms.CharField(label='البريد الالكتروني')
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'who_iam','specialist','subtitle','number_phone','address','price','working_hours','facebook','google','twitter','waiting_time','image','gender']




class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfilePatient
        fields = '__all__'
