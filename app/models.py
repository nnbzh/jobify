from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=3)

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"


