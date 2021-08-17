from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('', views.registration, name = 'registration'),
    path('login/', views.user_login, name = 'user_login'),
    path('profile/', views.profile, name = 'profile'),
    path('change_password/', views.change_password, name = 'change_password'),
]