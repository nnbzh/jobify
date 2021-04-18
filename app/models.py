from django.db import models


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"