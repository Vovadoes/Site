from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"type":"Password", "required placeholder":"Пароль", 'class': 'field'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={"type":"Repeat_password", "required placeholder":"Повторите пароль", 'class': 'field'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        widgets={
            'username': forms.TextInput(attrs={"type":"username", "required placeholder":"Логин", 'class': 'field'}),
            'first_name': forms.TextInput(attrs={"type":"first_name", "required placeholder":"Имя", 'class': 'field'}),
            'email': forms.TextInput(attrs={"type":"email", "required placeholder":"Email", 'class': 'field'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"type":"login", "required placeholder":"Логин"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"type":"password", "required placeholder":"Пароль"}))