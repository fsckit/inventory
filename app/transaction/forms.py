from django import forms
from app.transaction.models import Transaction

class TransactionForm(forms.ModelForm):
  def clean_item(self):
    data = self.cleaned_data['item']
    raise Exception('cleaner')
    if data == None:
      raise forms.ValidationError("Item does not exist.")

    return data

  def clean_customer(self):
    data = self.cleaned_data['customer']
    if data == None:
      raise forms.ValidationError("Customer does not exist.")

    return data

  def clean(self):
    cleaned_data = super(TransactionForm, self).clean()

    # Verify that current state is appropriate for this transaction type.
    action = cleaned_data.get('action')
    c = cleaned_data.get('customer')
    i = cleaned_data.get('item')

    # If either the item or customer were not provided, they will already have
    # validation errors, so we can skip this
    if c is None or i is None:
      return cleaned_data

    t = i.latest_tran()

    if action == 'c':
      # claim: there must be at least one prior transaction (since it has to be lent)
      if t is None:
        raise forms.ValidationError('Item not lent to con')

      # claim: item.owner must be the selected customer
      if i.owner != c:
        raise forms.ValidationError('Selected customer not item owner')

      # claim: item must be not currently borrowed, so last action must be 'return' or 'lend'
      if t.action != 'l' and t.action != 'r':
        raise forms.ValidationError('Item currently borrowed')

    elif action == 'l':
      # claim: either there are no transactions or the last transaction was claim.
      # so, it fails if there are transactions and the last transaction was not claim.
      if t is not None and t.action != 'c':
        raise forms.ValidationError('Item not supposed to be held by customer')

    elif action == 'b':
      # claim: item must be in con's possession, so last action must be lend or return
       # claim: there must be at least one prior transaction (since it has to be lent)
      if t is None:
        raise forms.ValidationError('Item not lent to con')
      if t.action != 'l' and t.action != 'r':
        raise forms.ValidationError('Item not available to lend')

    elif action == 'r':
      # claim: item must currently be borrowed by the customer.
      # This method of doing this isn't that good, but can't really think of better
      # one pending code review.
      # claim: there must be at least one prior transaction (since it has to be lent)
      if t is None:
        raise forms.ValidationError('Item not lent to con')
      if t.action != 'b' or t.customer != c:
        raise forms.ValidationError('Item not borrowed by selected customer')

    return cleaned_data

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
