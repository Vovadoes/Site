from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)