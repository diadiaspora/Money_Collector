from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Account
from .forms import TransactionForm

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

  transaction_form = TransactionForm()
  return render(request, 'accounts/detail.html', {
        # include the cat and feeding_form in the context
        'account': account, 'transaction_form': transaction_form
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
