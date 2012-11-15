from django import forms

class SearchForm(forms.Form):
  # cust_info -> (items owned by, items held by)
  cust_name = forms.CharField(required=False)

  # item_info -> customers
  item_name = forms.CharField(required=False)
  item_label = forms.CharField(required=False)
