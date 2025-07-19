# case_create/models.py
from django.db import models

class CaseLink(models.Model):
    link = models.URLField()

    def __str__(self):
        return self.link