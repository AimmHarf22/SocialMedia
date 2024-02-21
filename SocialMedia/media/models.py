from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Users(AbstractUser):
    # TODO: finish fixing the models
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.AbstractUser.email(blank=False)
    username = models.AbstractUser.username(blank=False)
    password = models.AbstractUser.password()
    