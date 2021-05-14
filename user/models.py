import os

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils import timezone

from user.managers import UserManager


def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"users/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"


class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    is_company = models.BooleanField('company status', default=False)
    avatar = models.ImageField(upload_to=upload_to, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
