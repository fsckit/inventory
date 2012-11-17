from django import forms

# Basic search form for handling queries
class SearchForm(forms.Form):
  qstr = forms.CharField()
