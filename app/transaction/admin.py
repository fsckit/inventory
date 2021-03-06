from django import forms
from django.contrib import admin
from app.transaction.models import Transaction

# Admin config for a transaction; uses Django's admin panel

class AdminForm(forms.ModelForm):
    class Meta:
        model = Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date','action','customer','item','signoff')
    form = AdminForm

admin.site.register(Transaction, TransactionAdmin)
