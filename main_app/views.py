from django.shortcuts import render

from django.http import HttpResponse

class Account:
  def __init__(self, bank, type, country, currency):
    self.bank = bank
    self.type = type
    self.country = country
    self.currency = currency

accounts = [
    Account('JP Morgan Chase', 'checking', 'United States', 'USD'),
    Account('Bank of America', 'savings', 'United States', 'USD'),
    Account('Santander', 'checking', 'Spain', 'EUR'),
    Account('Banco Popular', 'checking', 'A4gentina', 'ARS')
]


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def account_index(request):
  return render(request, 'accounts/index.html', {'accounts': accounts})