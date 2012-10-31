from django import forms
from app.item.models import Item

class ItemCreate(forms.ModelForm):
  label_id = forms.CharField(label='Id')
  
  class Meta:
    model = Item  
