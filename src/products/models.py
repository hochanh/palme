from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)

    price = models.DecimalField(max_digits=19, decimal_places=4)

    def __str__(self):
        return f"{self.name} ${self.price:.02f}"
