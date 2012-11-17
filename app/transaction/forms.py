from django import forms
from app.transaction.models import Transaction

class TransactionForm(forms.ModelForm):

  class Meta:
    model = Transaction
    fields = ['action', 'customer', 'item']
    widgets = {
        'customer': forms.widgets.TextInput(attrs={'autocomplete':'off'}),
        'item': forms.widgets.TextInput(attrs={'autocomplete':'off'}),
    }
