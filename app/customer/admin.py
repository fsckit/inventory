from django import forms
from django.contrib import admin
from app.customer.models import Customer

class AdminForm(forms.ModelForm):
    class Meta:
        model = Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','student_id','phone_number')
    form = AdminForm

admin.site.register(Customer, CustomerAdmin)
