from django.db import models


class CompanyManager(models.Manager):

    def vacancy_count(self):
        return self.vacancies.count()