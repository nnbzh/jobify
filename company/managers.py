from django.db import models


class CompanyManager(models.Manager):

    def vacancy_count(self):
        return self.vacancies.count()

    def add_contact(self, contact_id):
        return self.update({
            'contact_id': contact_id
        })
