from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from app.decorators import json_response, staff_only
from app.item.forms import ItemCreate
from app.item.models import Item
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Controller for items: recieves a request, interfaces with the database,
# and renders the template result for the view

# List all items
@staff_only
def index(request):
  items = Item.objects.all().order_by('name')
  return render_to_response('item/index.html', {'items': items}, context_instance=RequestContext(request))

# Create new item
@staff_only
@json_response('POST')
def create(request):
  # POST flag discriminates submission from form request
  if request.method == 'POST':
    form = ItemCreate(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return { 'success': True }
    # Form was invalid
    return { 'success': False }
  else:
    # Just show the form to the user
    form = ItemCreate()
    return render_to_response('item/create.html', {'form': form}, context_instance=RequestContext(request))

# Show an individual item's details.
@staff_only
def read(request, id = -1):
  # Fetch from the database
  item = Item.objects.get(pk=id)
  return render_to_response('item/read.html', {'item': item}, context_instance=RequestContext(request))

# Update a item -- stub; may not implement
@staff_only
@json_response('POST')
def update(request, id = -1):
  item = Item.objects.get(pk=id)
  # POST flag discriminates submission from form request
  if request.method == 'POST':
    form = ItemCreate(request.POST, request.FILES, instance=item)
    if form.is_valid():
      form.save()
      return { 'success': True }
    # Form was invalid
    return { 'success': False }
  else:
    # Create a form based on the instance of the customer found
    form = ItemCreate(instance=item)
    return render_to_response('item/update.html', {'form': form}, context_instance=RequestContext(request))

# Delete a item -- stub; may not implement
@staff_only
@json_response('POST')
def delete(request, id = -1):
  return { 'route': request.path }
