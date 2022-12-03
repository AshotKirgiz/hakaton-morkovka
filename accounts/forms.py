from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class RegisterUserForm(UserCreationForm):

    full_name = forms.CharField(label='ФИО', widget=forms.TextInput(attrs={'class': 'form-input'}))
    job_title = forms.CharField(label='Должность автора', widget=forms.TextInput(attrs={'class': 'form-input'}))
    job = forms.CharField(label='Место работы', widget=forms.TextInput(attrs={'class': 'form-input'}))
    theme = forms.CharField(label='Ссылка на ваш информационный ресурс', widget=forms.TextInput(attrs={'class': 'form-input'}))
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    media = forms.FileField(label='Прикрепить файл', widget=forms.FileInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = (
            'full_name', 'job_title', 'job', 'theme', 'username', 'password1', 'media'
        )