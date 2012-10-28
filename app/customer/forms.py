from django import forms

class TakeItemForm(forms.Form):
  item_id = forms.IntegerField()
