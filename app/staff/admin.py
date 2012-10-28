from django import forms
from django.contrib import admin
from django.contrib.auth.models import User

class AdminForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('user',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','first_name','last_name')
    form = AdminForm

admin.site.register(Profile, ProfileAdmin)
