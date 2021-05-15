from django.db import models


# Create your models here.
from company.models import Company


class ExperienceType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Experience Type"
        verbose_name_plural = "Experience Types"


class BusinessType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Busyness Type"
        verbose_name_plural = "Busyness Types"


class Vacancy(models.Model):
    name = models.CharField(max_length=512)
    experience_type = models.ForeignKey(ExperienceType, on_delete=models.CASCADE, related_name="vacancy")
    business_type = models.ForeignKey(BusinessType, on_delete=models.CASCADE, related_name="vacancy")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"


class Responsibility(models.Model):
    name = models.CharField(max_length=512)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="responsibilities")

    class Meta:
        verbose_name = "Responsibility"
        verbose_name_plural = "Responsibilities"


class Requirement(models.Model):
    name = models.CharField(max_length=512)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="requirements")

    class Meta:
        verbose_name = "Requirement"
        verbose_name_plural = "Requirements"


class Condition(models.Model):
    name = models.CharField(max_length=512)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="conditions")

    class Meta:
        verbose_name = "Condition"
        verbose_name_plural = "Conditions"
