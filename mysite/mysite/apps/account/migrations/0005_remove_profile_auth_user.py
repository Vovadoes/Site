# Generated by Django 3.2.5 on 2021-08-15 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_profile_auth_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='auth_user',
        ),
    ]