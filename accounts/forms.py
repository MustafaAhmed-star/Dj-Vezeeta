from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم')
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']



class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الثاني')
    email = forms.EmailField(label='البريد الالكتروني')
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]
