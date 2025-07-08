from django.db import models

# Create your models here.

class Account(models.Model):
    bank = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    country = models.CharField(max_length=250)
    currency = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.bank} ({self.id})"
