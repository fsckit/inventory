from app.decorators import json_response, staff_only
from django.db.models import Max, F
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from app.customer.forms import CreateForm
from app.customer.models import Customer
from app.transaction.models import Transaction

# Controller for customer: recieves a request, interfaces with the database,
# and renders the template result for the view

# List all customers
@staff_only
def index(request):
  customer = Customer.objects.all().order_by('last_name')
  return render_to_response('customer/index.html', {'customer': customer}, context_instance=RequestContext(request))

# List customers that need to return an item
def summary(request):
  # Limit transactions to only those that were the latest for their given item,
  # then join and return
  latest_transactions = Transaction.objects \
    .annotate(latest=Max('item__transaction__date')) \
    .filter(latest=F('date')) \
    .select_related('item') \
    .select_related('customer') \
    .filter(action='b') # Only care about borrowed items

  customers = [(t.item, t) for t in latest_transactions]

  return render_to_response('customer/summary.html', {'customers': customers}, context_instance=RequestContext(request))

# Create new customer
@staff_only
@json_response('POST')
def create(request):
  # POST flag discriminates submission from form request
  if request.method == 'POST':
    form = CreateForm(request.POST, request.FILES)
    if form.is_valid():
      obj = form.save()
      return { 'success': True, 'message': "Customer '%s' added" % form.instance.full_name }
    # Form was invalid
    return { 'success': False, 'errors': form.errors }
  else:
    # Just show the form to the user
    form = CreateForm()
    return render_to_response('customer/create.html', {'form': form}, context_instance=RequestContext(request))

# Read a single customer
@staff_only
def read(request, id=-1):
  # Fetch from the database
  try:
    customer = Customer.objects.get(pk=id)
  except ObjectDoesNotExist:
    raise Http404
  return render_to_response('customer/read.html', {'customer': customer}, context_instance=RequestContext(request))

# Update a customer
@staff_only
@json_response('POST')
def update(request, id=-1):
  # Find related model -- will raise error if not found
  try:
    customer = Customer.objects.get(pk=id)
  except ObjectDoesNotExist:
    raise Http404
  if request.method == 'POST':
    form = CreateForm(request.POST, request.FILES, instance=customer)
    if form.is_valid():
      obj = form.save()
      return { 'success': True, 'message': "Customer '%s' updated" % form.instance.full_name }
    # Invalid form
    return { 'success': False, 'errors': form.errors }
  else:
    # Create a form based on the instance of the customer found
    form = CreateForm(instance=customer)
    return render_to_response('customer/update.html', {'form': form}, context_instance=RequestContext(request))

# Delete a customer -- stub; may not implement
@json_response('POST')
def delete(request, id = -1):
  return { 'route': request.path }
