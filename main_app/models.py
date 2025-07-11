from django.db import models
from django.urls import reverse

# Create your models here.

class Account(models.Model):
    bank = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    country = models.CharField(max_length=250)
    currency = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.bank} ({self.id})"

    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('account-detail', kwargs={'account_id': self.id})