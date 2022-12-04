from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    fio = forms.CharField(label='ФИО', widget=forms.TextInput(attrs={'class': 'form-input'}))
    job = forms.CharField(label='Местоработы и доллжность', widget=forms.TextInput(attrs={'class': 'form-input'}))
    theme = forms.CharField(label='Тема и аннотация', widget=forms.TextInput(attrs={'class': 'form-input'}))
    media = forms.CharField(label='Ссылка на материал', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = CustomUser
        fields = (
            'username', 'password1', 'password2', 'fio', 'job', 'theme', 'media'
        )



class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')