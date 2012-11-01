from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from app.item.forms import ItemCreate
from app.item.models import Item
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

def index(request):
  items = [(item.name, item.pk) for item in Item.objects.all()]
  return render_to_response('item/item_index.html', {'items': items}, context_instance=RequestContext(request))

def create(request):
  if request.method == 'POST':
    form = ItemCreate(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')
  else:
    form = ItemCreate()
  return render_to_response('item/item_create.html', {'form': form}, context_instance=RequestContext(request))

# Show an individual item's details.
def read(request, id = -1):
  item = Item.objects.filter(pk=id)
  # TODO: Show an error if the item isn't found (I'm lazy)
  return render_to_response('item/item_read.html', {'item': item[0]}, context_instance=RequestContext(request))

# List of items (stub)
def list_items(request):
  return render_to_response('item/item_read.html', context_instance=RequestContext(request))

def update(request, id = -1):
  if request.method == 'POST':
    form = ItemCreate(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('item_read'))
  else:
    form = ItemCreate()
  return render_to_response('item/item_update.html', {'form': form}, context_instance=RequestContext(request))

def delete(request, id = -1):
  return render_to_response('item/item_delete.html', context_instance=RequestContext(request))
