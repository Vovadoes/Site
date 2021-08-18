from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        widgets={
            'username': forms.TextInput(attrs={"placeholder":"Логин", 'class': 'field'}),
            'first_name': forms.TextInput(attrs={"placeholder":"Имя", 'class': 'field'}),
            'email': forms.TextInput(attrs={"placeholder":"Email", 'class': 'field'}),
        }

    def __iadd__(self, other):
        if other.username != None:
            self.username = other.username
        if other.first_name != None:
            self.first_name = other.first_name
        if other.email != None:
            self.email = other.email


class LoginForm(forms.Form):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"type":"login", "placeholder":"Логин", 'class': 'field'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"type":"password", "placeholder":"Пароль", 'class': 'field'}))


class PasswordForm(forms.Form):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"placeholder":"Пароль", 'class': 'field'}))
    password2 = forms.CharField(label='Повторите Пароль', widget=forms.PasswordInput(attrs={"placeholder":"Повторите пароль", 'class': 'field'}))

    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']