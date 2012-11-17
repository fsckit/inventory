from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from app.decorators import json_response, staff_only, superuser_only
from app.staff.forms import CreateForm, UpdateForm
from app.staff.forms import ActivationForm
from django.core.mail import send_mail
from django.utils.hashcompat import sha_constructor
from random import randint as rng
from django.core.exceptions import ObjectDoesNotExist
from django.core import mail

# Controller for staff: recieves a request, interfaces with the database,
# and renders the template result for the view

# List all staff
@staff_only
def read(request, id=-1):
  user = User.objects.get(pk=id)
  return render_to_response('staff/read.html', {'user': user}, context_instance=RequestContext(request))

# Create new staff
@superuser_only
def create(request):
  # POST flag discriminates submission from form request
  if request.method == 'POST':
    form = CreateForm(request.POST, request.FILES)
    if form.is_valid():
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
    # Just show the form to the user
    form = CreateForm()
    return render_to_response('staff/create.html', {'form': form}, context_instance=RequestContext(request))

# Changes for activation
def activation(request, activation_key=None):
  # Check if users exists
  try:
    user = User.objects.get(password=activation_key)
  except ObjectDoesNotExist:
    raise Http404
  # POST flag discriminates submission from form request
  if request.method == 'POST':
    form = ActivationForm(request.POST, request.FILES)
    if form.is_valid():
      # Set password specifically using Django's method
      user.set_password(form.cleaned_data['password'])
      user.save()
      # Log the user in immediately after activation
      user = authenticate(username=user.username, password=form.cleaned_data['password'])
      # Verify that the authentication was successful
      if user is not None:
        # If the staff account was not deactivated, do the login
        if user.is_active:
          login(request, user)
        else:
          # Error
          return HttpResponseNotFound("User is inactive")
      else:
        # Error
        return HttpResponseNotFound("Invalid login")
      # Redirect the staff member to the stage
      return HttpResponseRedirect(reverse('home'))
  else:
    # Just show the form to the user
    form = ActivationForm()
    return render_to_response('staff/activation.html', {'form': form, 'activation_key': activation_key}, context_instance=RequestContext(request))

# Displays a success page for the superuser creating the email
def email_sent(request):
  return render_to_response('staff/email_sent.html', {}, context_instance=RequestContext(request))

# Update a staff member
def update(request):
  # Update defaults to self (request.user)
  if request.method == 'POST':
    form = UpdateForm(request.POST, request.FILES, instance=request.user)
    if form.is_valid():
      form.save(commit=False)
      # If a password was specified (optional), change it
      if len(form.cleaned_data['password']) > 0:
        request.user.set_password(form.cleaned_data['password'])
      request.user.save()
      # This is not ajax, so redirect them back to the stage
      return HttpResponseRedirect(reverse('home'))
  else:
    # Create a form based on the instance of the customer found
    form = UpdateForm(instance=request.user)
    return render_to_response('staff/update.html', {'form': form}, context_instance=RequestContext(request))
