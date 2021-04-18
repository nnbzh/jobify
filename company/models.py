from django.db import models

# Create your models here.
from app.models import Region
from company.managers import CompanyManager


class Company(models.Model):
    name = models.CharField(max_length=512)
    bin = models.IntegerField()
    description = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="company")
    create_date = models.DateTimeField(blank=True)

    object = CompanyManager()

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class ContactType(models.Model):
    name = models.CharField(max_length=512)

    class Meta:
        verbose_name = "Contact Type"
        verbose_name_plural = "Contact Types"


class Contact(models.Model):
    value = models.CharField(max_length=512)
    contact_type = models.ForeignKey(ContactType, on_delete=models.CASCADE, related_name="contact")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="contacts")

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
