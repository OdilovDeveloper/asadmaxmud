from django.db import models

class LiveLink(models.Model):
    link = models.URLField("Jonli efir havolasi", max_length=300)

    def __str__(self):
        return self.link