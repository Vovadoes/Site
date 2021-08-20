from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo', )


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        required = {
            'username' : False,
            'first_name': False,
            'email' : False
        }
        widgets={
            'username': forms.TextInput(attrs={"placeholder":"Логин", 'class': 'field'}),
            'first_name': forms.TextInput(attrs={"placeholder":"Имя", 'class': 'field'}),
            'email': forms.TextInput(attrs={"placeholder":"Email", 'class': 'field'}),
        }


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