from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


# User = get_user_model()
#
#
# class Profile(models.Model):
#     desc = models.CharField(max_length=100, null=True, blank=True)
#     user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='profile')

class MyUser(AbstractUser):
    desc = models.CharField(max_length=100, null=True, blank=True)


class Book(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()