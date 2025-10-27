from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
class Crypto(models.Model):
    name = models.CharField(max_length=50)
    price_usd = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('crypto-detail', kwargs={'pk': self.id})

  

class Account(models.Model):
    bank = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    country = models.CharField(max_length=250)
    currency = models.CharField(max_length=100)
    crypto = models.ManyToManyField(Crypto)

    def __str__(self):
        return f"{self.account.bank} ({self.id})"
    
    def get_balance(self):
        deposits = self.transaction_set.filter(type='D').aggregate(models.Sum('amount'))['amount__sum'] or 0
        withdrawals = self.transaction_set.filter(type='W').aggregate(models.Sum('amount'))['amount__sum'] or 0
        transfers = self.transaction_set.filter(type='T').aggregate(models.Sum('amount'))['amount__sum'] or 0  # Optional
        return deposits - withdrawals - transfers  # Adjust logic if transfer isn't outflow


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
    amount = models.DecimalField(max_digits=12, decimal_places=2) 

    def __str__(self):
        
      return f"{self.get_type_display()} on {self.date}"
    
    def get_absolute_url(self):
        return reverse('account-detail', kwargs={'account_id': self.id})
    
    class Meta:
        ordering = ['-date'] 

    


class Transfer(models.Model):
    from_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transfers_out')
    to_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transfers_in')
    date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Transfer ${self.amount} from {self.from_account} to {self.to_account} on {self.date}"
