from django import forms
from app.customer.models import Customer

# Basic customer creation/update form

class CreateForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ('first_name', 'last_name', 'email', 'student_id', 'phone_number')
