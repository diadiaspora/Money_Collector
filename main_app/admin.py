from django.contrib import admin
from .models import Account, Transaction, Crypto
# Register your models here.
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Crypto)