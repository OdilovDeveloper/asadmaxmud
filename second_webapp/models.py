from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='second_webapp/')

    def __str__(self):
        return self.title