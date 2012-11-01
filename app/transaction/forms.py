from django import forms
from app.transaction.models import Transaction

class TransactionForm(forms.ModelForm):

  class Meta:
    model = Transaction
    fields = ['action', 'customer', 'item']
