from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Account, Crypto
from .forms import TransactionForm

class AccountCreate(CreateView):
    model = Account
    fields =  ['bank', 'type', 'country', 'currency']

class CryptoCreate(CreateView):
      model = Crypto
      fields = '__all__'

class AccountUpdate(UpdateView):
    model = Account
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['bank', 'type', 'country', 'currency']

class AccountDelete(DeleteView):
    model = Account
    success_url = '/accounts/'

class CryptoList(ListView):
    model = Crypto

class CryptoDetail(DetailView):
    model = Crypto

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
  cryptos_account_doesnt_have = Crypto.objects.exclude(id__in = account.crypto.all().values_list('id'))
  transaction_form = TransactionForm()
  return render(request, 'accounts/detail.html', {
        'account': account, 
        'transaction_form': transaction_form,
        'cryptos' : cryptos_account_doesnt_have
    })

def add_transaction(request, account_id):
    # create a ModelForm instance using the data in request.POST
    form = TransactionForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_transaction = form.save(commit=False)
        new_transaction.account_id = account_id
        new_transaction.save()
    return redirect('account-detail', account_id=account_id)

class CryptoUpdate(UpdateView):
    model = Crypto
    fields = ['name', 'price_usd']

class CryptoDelete(DeleteView):
    model = Crypto
    success_url = '/crypto/'

def associate_crypto(request, account_id, crypto_id):
    Account.objects.get(id=account_id).cryptos.add(crypto_id)
    return redirect('account-detail', account_id=account_id)

def remove_crypto(request, account_id, crypto_id):
    account = get_object_or_404(Account, id=account_id)
    crypto = get_object_or_404(Crypto, id=crypto_id)
    account.crypto.remove(crypto)
    return redirect('account-detail', account_id=account.id)