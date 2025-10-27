from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'type', 'amount']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
           'amount': forms.NumberInput(attrs={  # ✅ Optional customization
                'placeholder': 'Enter amount',
                'min': '0.01',
                'step': '0.01'
            })
        }