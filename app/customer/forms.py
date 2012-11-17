from django import forms
from app.customer.models import Customer

class CreateForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ('full_name', 'email', 'student_id', 'phone_number')
