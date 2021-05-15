from django.db import models


class CompanyManager(models.Manager):

    def vacancy_count(self):
        return self.vacancies.count()

    def add_contact(self, company_id, value):
        return self.filter(id=company_id).get().contact.create(company_id=company_id, value=value)
