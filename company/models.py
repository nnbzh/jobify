from django.db import models

# Create your models here.
from app.models import Region
from company.managers import CompanyManager
from user.models import User


class Contact(models.Model):
    value = models.CharField(max_length=512)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class Company(models.Model):
    name = models.CharField(max_length=512)
    bin = models.IntegerField()
    description = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="company")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="company")
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="company", blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    objects = CompanyManager()

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
