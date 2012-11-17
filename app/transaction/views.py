from app.decorators import json_response, staff_only
from app.transaction.forms import TransactionForm
from django.db.models import Max
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from app.transaction.models import Transaction
from app.transaction.email import SendMessage
from uuid import uuid1 as guid

from app.item.models import Item


# Get latest transaction on some item i.
def latest_tran(i):
  last_tran_dt = Transaction.objects.filter(item=i).aggregate(Max('date'))['date__max']
  try:
    return Transaction.objects.get(item=i, date=last_tran_dt)
  except ObjectDoesNotExist:
    return None

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
      # Verify that current state is appropriate for this transaction type.
      action = form.cleaned_data['action']
      c = form.cleaned_data['customer']
      i = form.cleaned_data['item']
      t = latest_tran(i)

      if action == 'c':
        # claim: there must be at least one prior transaction (since it has to be lent)
        if t is None:
          return {'success': False, 'reason': 'Item not lent to con'}

        # claim: item.owner must be the selected customer
        if i.owner != c:
          return {'success': False, 'reason': 'Selected customer not item owner'}

        # claim: item must be not currently borrowed, so last action must be 'return' or 'lend'
        if t.action != 'l' and t.action != 'r':
          return {'success': False, 'reason': 'Item currently borrowed'}

      elif action == 'l':
        # claim: either there are no transactions or the last transaction was claim.
        # so, it fails if there are transactions and the last transaction was not claim.
        t = latest_tran(i)
        if t is not None and t.action != 'c':
          return {'success': False, 'reason': 'Item not supposed to be held by customer'}

      elif action == 'b':
        # claim: item must be in con's possession, so last action must be lend or return
         # claim: there must be at least one prior transaction (since it has to be lent)
        if t is None:
          return {'success': False, 'reason': 'Item not lent to con'}
        t = latest_tran(i)
        if t.action != 'l' and t.action != 'r':
          return {'success': False, 'reason': 'Item not available to lend'}

      elif action == 'r':
        # claim: item must currently be borrowed by the customer.
        # This method of doing this isn't that good, but can't really think of better
        # one pending code review.
        # claim: there must be at least one prior transaction (since it has to be lent)
        if t is None:
          return {'success': False, 'reason': 'Item not lent to con'}
        if last_tran.action != 'b' or last_tran.customer != c:
          return {'success': False, 'reason': 'Item not borrowed by selected customer'}

      # Add the current staff member as a signoff
      form.instance.signoff = request.user

      # Email receipt
      form.instance.id = guid().int
      instance = form.save()

      # Call SendMessage in email module
      SendMessage(instance)

      return { 'success': True }
    # Form was invalid
    return { 'success': False }
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
@json_response
def update(request, id = -1):
  return { 'route': request.path }

# Delete a tranasction -- stub; may not implement
@staff_only
@json_response
def delete(request, id = -1):
  return { 'route': request.path }
