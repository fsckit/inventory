from django.db.models import Max, F
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.http import Http404
from django.core.urlresolvers import reverse
from app.decorators import json_response, staff_only
from app.item.forms import ItemCreate
from app.item.models import Item
from app.transaction.models import Transaction

# Controller for items: recieves a request, interfaces with the database,
# and renders the template result for the view

# List all items
@staff_only
def index(request):
  items = Item.objects.all().order_by('name')
  return render_to_response('item/index.html', {'items': items}, context_instance=RequestContext(request))

# List items that need to be returned
def summary(request):
  # Limit transactions to only those that were the latest for their given item,
  # then join and return
  latest_transactions = Transaction.objects \
    .annotate(latest=Max('item__transaction__date')) \
    .filter(latest=F('date')) \
    .select_related('item') \
    .exclude(action='c') # Don't care about claimed items

  # Group them into 'loaned' and 'stocked': the former being the item out to
  # another customer, and the latter being in the con's inventory
  items = { 'loaned': [], 'stocked': [] }

  for t in latest_transactions:
    if t.action == 'b':
      items['loaned'].append((t.item, t))
    else:
      items['stocked'].append((t.item, t))

  return render_to_response('item/summary.html', {'items': items}, context_instance=RequestContext(request))

# Create new item
@staff_only
@json_response('POST')
def create(request):
  # POST flag discriminates submission from form request
  if request.method == 'POST':
    form = ItemCreate(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return { 'success': True, 'message': "Item '%s' created" % form.instance.name }
    # Form was invalid
    return { 'success': False, 'errors': form.errors }
  else:
    # Just show the form to the user
    form = ItemCreate()
    return render_to_response('item/create.html', {'form': form}, context_instance=RequestContext(request))

# Show an individual item's details.
@staff_only
def read(request, id = -1):
  # Fetch from the database
  try:
    item = Item.objects.get(pk=id)
  except ObjectDoesNotExist:
    raise Http404
  return render_to_response('item/read.html', {'item': item}, context_instance=RequestContext(request))

# Update a item -- stub; may not implement
@staff_only
@json_response('POST')
def update(request, id = -1):
  try:
    item = Item.objects.get(pk=id)
  except ObjectDoesNotExist:
    raise Http404
  # POST flag discriminates submission from form request
  if request.method == 'POST':
    form = ItemCreate(request.POST, request.FILES, instance=item)
    if form.is_valid():
      form.save()
      return { 'success': True, 'message': "Item '%s' updated" % form.instance.name }
    # Form was invalid
    return { 'success': False, 'errors': form.errors }
  else:
    # Create a form based on the instance of the customer found
    form = ItemCreate(instance=item)
    return render_to_response('item/update.html', {'form': form}, context_instance=RequestContext(request))

# Delete a item -- stub; may not implement
@staff_only
@json_response('POST')
def delete(request, id = -1):
  return { 'route': request.path }
