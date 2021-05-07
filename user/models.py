from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from user.managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    is_company = models.BooleanField('company status', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

