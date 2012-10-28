from django import forms
from django.contrib.auth.models import User

class CreateForm(forms.ModelForm):
  # Required fields
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'password', 'is_superuser')
    widgets = {
        'email':    forms.widgets.TextInput(attrs={'autocomplete':'off'}),
        'password': forms.widgets.PasswordInput(attrs={'autocomplete':'off'}),
    }
