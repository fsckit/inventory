from random import randrange
from django.db.models import Max
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from app.decorators import json_response, staff_only
from app.transaction.forms import TransactionForm
from app.transaction.models import Transaction
from app.transaction.email import SendMessage
from app.item.models import Item



# Controller for transaction: recieves a request, interfaces with the database,
# and renders the template result for the view

# List all transactions
@staff_only
def index(request):
  transactions = Transaction.objects.all()
  return render_to_response('transaction/index.html', {'transactions': transactions}, context_instance=RequestContext(request))

# Create new transaction
@staff_only
@json_response('POST')
def create(request):
  # POST flag discriminates submission from form request
  if request.method == 'POST':
    form = TransactionForm(request.POST, request.FILES)

    if form.is_valid():
      # Add the current staff member as a signoff
      form.instance.signoff = request.user

      # Email receipt
      form.instance.id = int(''.join(str(randrange(10)) for i in range(9)))
      instance = form.save()
      instance.send_email()

      return { 'success': True }
    # Form was invalid
    return { 'success': False, 'errors': form.errors }
  else:
    # Just show the form to the user
    form = TransactionForm()
    return render_to_response('transaction/create.html', {'form': form}, context_instance=RequestContext(request))

# Read a single transaction
@staff_only
def read(request, id = -1):
  # Fetch from the database
  qs = Transaction.objects.get(pk=id)
  return render_to_response('transaction/read.html', {'o': qs}, context_instance=RequestContext(request))

# Update a tranasction -- stub; may not implement
@staff_only
@json_response('POST')
def update(request, id = -1):
  return { 'route': request.path }

# Delete a tranasction -- stub; may not implement
@staff_only
@json_response('POST')
def delete(request, id = -1):
  return { 'route': request.path }
