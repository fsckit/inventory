from django import forms
from django.contrib.auth.models import User

# Form for creating a new staff from a superuser staff
class CreateForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'is_superuser',)
    widgets = {
        # Special widget to disable autocomplete 
        'email': forms.widgets.TextInput(attrs={'autocomplete':'off'})
    }

# Form for activating a staff member and setting his/her password
class ActivationForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('password',)#, 'password_confirmation')
    widgets = {
        'password':	forms.widgets.PasswordInput()
        #'password_confirmation': forms.widgets.TextInput(attrs={'autocomplete':'off'}),
    }

# Update form is similar to CreateForm but allows password update
class UpdateForm(forms.ModelForm):
  # Special field with label; not bound to model so we can use set_password()
  password = forms.CharField(widget=forms.PasswordInput, label="New Password", required=False)
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email')
