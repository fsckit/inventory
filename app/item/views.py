from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from app.item.forms import ItemCreate
from app.item.models import Item
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

def index(request):
  items = [(item.name, item.label_id) for item in Item.objects.all()]
  return render_to_response('item/index.html', {'items': items}, context_instance=RequestContext(request))

def create(request):
  if request.method == 'POST':
    form = ItemCreate(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')
  else:
    form = ItemCreate()
  return render_to_response('item/create.html', {'form': form}, context_instance=RequestContext(request))

# Show an individual item's details.
def read(request, id = -1):
  item = Item.objects.get(label_id=id)
  return render_to_response('item/read.html', {'item': item}, context_instance=RequestContext(request))

# List of items (stub)
def list_items(request):
  return render_to_response('item/read.html', context_instance=RequestContext(request))

def update(request, id = -1):
  item = Item.objects.get(label_id=id)
  if request.method == 'POST':
    form = ItemCreate(request.POST, request.FILES, instance=item)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('item_read', args=[item.label_id]))
  else:
     form = ItemCreate(instance=item)
  return render_to_response('item/update.html', {'form': form}, context_instance=RequestContext(request))

def delete(request, id = -1):
  return render_to_response('item/delete.html', context_instance=RequestContext(request))
