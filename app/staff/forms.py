from django import forms
from django.contrib.auth.models import User

class CreateForm(forms.ModelForm):
  # Required fields
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'is_superuser',)
    widgets = {
        'email':    forms.widgets.TextInput(attrs={'autocomplete':'off'})
    }

class ActivationForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('password',)#, 'password_confirmation')
    widgets = {
        'password':	forms.widgets.PasswordInput()
        #'password_confirmation': forms.widgets.TextInput(attrs={'autocomplete':'off'}),
    }

class UpdateForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput, label="New Password", required=False)
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email')
