from django.db import models
from django.urls import reverse

# Create your models here.

class Account(models.Model):
    bank = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    country = models.CharField(max_length=250)
    currency = models.CharField(max_length=100)

# Add new Feeding model below Cat model

ACTIONS = (
    ('D', 'Deposit'),
    ('W', 'Withdrawl'),
    ('T', 'Transfer')
)



class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(
       max_length=1,
    choices=ACTIONS,
    default=ACTIONS[0][0]
    )    

    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_type_display()} on {self.date}"
    
    
    def __str__(self):
        return f"{self.account.bank} ({self.id})"

    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('account-detail', kwargs={'account_id': self.id})
    
    class Meta:
        ordering = ['-date'] 

    
class Crypto(models.Model):
    name = models.CharField(max_length=50)
    price_usd = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('crypto-detail', kwargs={'pk': self.id})
