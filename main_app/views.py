from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Account

class AccountCreate(CreateView):
    model = Account
    fields = '__all__'

class AccountUpdate(UpdateView):
    model = Account
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['bank', 'type', 'country', 'currency']

class AccountDelete(DeleteView):
    model = Account
    success_url = '/accounts/'

# from django.http import HttpResponse

# class Account:
#   def __init__(self, bank, type, country, currency):
#     self.bank = bank
#     self.type = type
#     self.country = country
#     self.currency = currency

# accounts = [
#     Account('JP Morgan Chase', 'checking', 'United States', 'USD'),
#     Account('Bank of America', 'savings', 'United States', 'USD'),
#     Account('Santander', 'checking', 'Spain', 'EUR'),
#     Account('Banco Popular', 'checking', 'A4gentina', 'ARS')
# ]


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def account_index(request):
  accounts = Account.objects.all()
  return render(request, 'accounts/index.html', {'accounts': accounts})

def account_detail(request, account_id):
  account = Account.objects.get(id=account_id)
  return render(request, 'accounts/detail.html', {'account': account})

