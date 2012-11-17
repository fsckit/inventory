from django import forms
from app.transaction.models import Transaction

class TransactionForm(forms.ModelForm):
  class Meta:
    model = Transaction
    # We omit the signoff field because that is added based on the user that
    # initiated the transaction
    fields = ['action', 'customer', 'item']
    # We also force the foreign keys to appear as searchable text widgets
    widgets = {
        'customer': forms.widgets.TextInput(attrs={'autocomplete':'off', 'class':'search'}),
        'item': forms.widgets.TextInput(attrs={'autocomplete':'off', 'class':'search'}),
    }
