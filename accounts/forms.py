from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': 'اسم المستخدم',
            'password1': 'كلمة المرور',
            'password2': 'تأكيد كلمة المرور',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'أدخل اسم المستخدم'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'أدخل كلمة المرور'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'أعد كتابة كلمة المرور'}),
        }
