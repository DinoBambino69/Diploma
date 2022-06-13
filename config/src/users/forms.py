from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from .models import UserProfiles

class RegisterUserForm(UserCreationForm):
    """Форма регистрации нового пользователя"""
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Логин'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Фамилия'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',  'password1', 'password2')


class AuthenticationUserForm(AuthenticationForm):
    """Форма аутентификации юзера"""
    username = forms.CharField( label='Login',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Логин'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Пароль'}))


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfiles
        exclude = ('user',)