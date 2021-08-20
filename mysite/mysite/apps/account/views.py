from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .forms import PasswordForm, UserRegistrationForm, ProfileForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import Profile, User


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('start:start'))
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        else:
            return HttpResponse('Не все поля заполнены')
    else:
        login_form = LoginForm()
    return render(request, 'account/login.html', {'login_form': login_form})


def registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        password = PasswordForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid() and password.is_valid() and password.clean_password2():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            new_profile = profile_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(password.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # --- 
            new_profile.user_id = new_user.id
            new_profile.save()
            return render(request, 'account/register_done.html')
        else:
            return HttpResponse('Не все поля заполнены или пароли не верны')
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
        password = PasswordForm()
    return render(request, 'account/register.html',
                {'user_form': user_form, 'profile_form': profile_form, 'password': password})

def profile(request):
    try:
        user = User.objects.get(id = request.user.id)
        profile = Profile.objects.get(id = request.user.profile.id)
    except:
        return HttpResponse('<h1>Войдите на сайт<h1>')

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, instance=user)
        profile_form = ProfileForm(instance=profile, data=request.POST, files=request.FILES)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            new_profile = profile_form.save(commit=False)
            if new_profile.photo == '':
                new_profile.photo = profile.photo
            new_profile.save()
        else:
            return HttpResponseRedirect(reverse('start:error'))
    profile = Profile.objects.get(id = request.user.profile.id)
    user_form = UserRegistrationForm(instance=User.objects.get(id = request.user.id))
    profile_form = ProfileForm(instance=profile)
    try:
        profile_photo_url = profile.photo.url
    except:
        profile_photo_url = profile.default_photo()
    return render(request, 'account/profile.html', {'profile_form': profile_form, 'user_form': user_form,
                'profile_photo_url': profile_photo_url})

def change_password(request):
    return HttpResponseRedirect(reverse('start:error'))