from django import forms
from django.contrib import admin
from app.item.models import Item

class AdminForm(forms.ModelForm):
    class Meta:
        model = Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','label_id','owner','type')
    form = AdminForm

admin.site.register(Item, ItemAdmin)
