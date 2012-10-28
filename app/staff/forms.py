from django import forms
from app.staff.models import Staff

class CreateForm(forms.ModelForm):
  class Meta:
    model = Staff
