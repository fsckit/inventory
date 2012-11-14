from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from app.decorators import json_response, staff_only, superuser_only
from app.staff.forms import CreateForm

@staff_only
def read(request, id=-1):
  user = User.objects.get(pk=id)
  return render_to_response('staff/read.html', {'user': user}, context_instance=RequestContext(request))

@superuser_only
def create(request):
  if request.method == 'POST':
    form = CreateForm(request.POST, request.FILES)
    if form.is_valid():
      # Create user object specially
      user = User.objects.create_user(form.cleaned_data['email'], form.cleaned_data['email'], form.cleaned_data['password'])
      # Set first and last name
      user.first_name = form.cleaned_data['first_name']
      user.last_name = form.cleaned_data['last_name']
      user.is_superuser = form.cleaned_data['is_superuser']
      return HttpResponseRedirect(reverse('staff_create'))
  else:
    form = CreateForm()

  return render_to_response('staff/create.html', {'form': form}, context_instance=RequestContext(request))

def update(request):
  # Update defaults to self (request.user)
  if request.method == 'POST':
    form = CreateForm(request.POST, request.FILES, instance=request.user)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('home'))
  else:
    form = CreateForm(instance=request.user)

  return render_to_response('staff/update.html', {'form': form}, context_instance=RequestContext(request))
