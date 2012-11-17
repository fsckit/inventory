from django import forms
from app.item.models import Item

class ItemCreate(forms.ModelForm):
  # Rename the label to provide a better description in the UI
  label_id = forms.CharField(label='Physical id')
  
  class Meta:
    model = Item  
    widgets = {
        # Change the select to a searchable input widget
        'owner': forms.widgets.TextInput(attrs={'autocomplete': 'off', 'class': 'search'}),
    }
