from django.db import models

# Create your models here.
from app.models import Region
from company.managers import CompanyManager
from user.models import User


class Company(models.Model):
    name = models.CharField(max_length=512)
    bin = models.IntegerField()
    description = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="company")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="company")
    create_date = models.DateTimeField(blank=True, null=True)

    objects = CompanyManager()

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class Contact(models.Model):
    value = models.CharField(max_length=512)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="contact")

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class Invite(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="invites")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="invites")

    class Meta:
        verbose_name = "Invite"
        verbose_name_plural = "Invites"


class Notification(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
