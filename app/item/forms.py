from django import forms
from app.item.models import Item

class ItemCreate(forms.ModelForm):
  label_id = forms.CharField(label='Physical id')
  
  class Meta:
    model = Item  
    widgets = {
        'owner': forms.widgets.TextInput(attrs={
          'autocomplete': 'off',
          'class': 'search',
        }),
    }
