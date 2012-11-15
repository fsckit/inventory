from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from app.decorators import json_response, staff_only, superuser_only
from app.staff.forms import CreateForm
from app.staff.forms import ActivationForm
from django.core.mail import send_mail
from django.utils.hashcompat import sha_constructor
from random import randint as rng
from django.core.exceptions import ObjectDoesNotExist


@staff_only
def read(request, id=-1):
  user = User.objects.get(pk=id)
  return render_to_response('staff/read.html', {'user': user}, context_instance=RequestContext(request))

@superuser_only
def create(request):
  if request.method == 'POST':
    form = CreateForm(request.POST, request.FILES)
    if form.is_valid():
      from django.core import mail
      connection = mail.get_connection('django.core.mail.backends.console.EmailBackend')
      connection.open()

      # generate activation key
      name = form.cleaned_data['first_name'] + form.cleaned_data['last_name']
      salt = (name[rng(0,int(len(name)/2)):rng(int(len(name)/2),len(name))] + name[::-1])
      activation_key = sha_constructor(salt + form.cleaned_data['email']).hexdigest()

      # Create user object specially
      user = User.objects.create_user(form.cleaned_data['email'], form.cleaned_data['email'])
      user.password = activation_key

      # Set first and last name
      user.first_name = form.cleaned_data['first_name']
      user.last_name = form.cleaned_data['last_name']
      user.is_superuser = form.cleaned_data['is_superuser']

      # generate message
      link = 'http://127.0.0.1:8000/staff/activation/'
      message = 'Go to ' + link + str(activation_key)
      mail.EmailMessage('Account Activation Link - Genericon Inventory Tracker', message, 'from@example.com', [form.cleaned_data['email']], connection=connection).send()
      connection.close()

      user.save()
      return HttpResponseRedirect(reverse('activation_email_sent'))
  else:
    form = CreateForm()

  return render_to_response('staff/create.html', {'form': form}, context_instance=RequestContext(request))

# Changes for activation

def activation(request, activation_key=None):
  try:
    user = User.objects.get(password=activation_key)
  except ObjectDoesNotExist:
    raise Http404
  if request.method == 'POST':
    form = ActivationForm(request.POST, request.FILES)
    if form.is_valid():
      user.set_password(form.cleaned_data['password'])
      user.save()
      user = authenticate(username=user.username, password=form.cleaned_data['password'])
      if user is not None:
        if user.is_active:
          login(request, user)
        else:
          return HttpResponseNotFound("User is inactive")
      else:
        return HttpResponseNotFound("Invalid login")
      return HttpResponseRedirect(reverse('home'))
  else:
    form = ActivationForm()

  return render_to_response('staff/activation.html', {'form': form, 'activation_key': activation_key}, context_instance=RequestContext(request))

def email_sent(request):
  return render_to_response('staff/email_sent.html', {}, context_instance=RequestContext(request))

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
