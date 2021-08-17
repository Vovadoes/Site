from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)