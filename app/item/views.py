from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from app.decorators import json_response, staff_only
from app.item.forms import ItemCreate
from app.item.models import Item
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

@staff_only
def index(request):
  items = Item.objects.all()
  return render_to_response('item/index.html', {'items': items}, context_instance=RequestContext(request))

@staff_only
@json_response('POST')
def create(request):
  if request.method == 'POST':
    form = ItemCreate(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return { 'success': True }
    return { 'success': False }
  else:
    form = ItemCreate()
  return render_to_response('item/create.html', {'form': form}, context_instance=RequestContext(request))

# Show an individual item's details.
@staff_only
def read(request, id = -1):
  item = Item.objects.get(pk=id)
  return render_to_response('item/read.html', {'item': item}, context_instance=RequestContext(request))

@staff_only
@json_response('POST')
def update(request, id = -1):
  item = Item.objects.get(pk=id)
  if request.method == 'POST':
    form = ItemCreate(request.POST, request.FILES, instance=item)
    if form.is_valid():
      form.save()
      return { 'success': True }
    return { 'success': False }
  else:
     form = ItemCreate(instance=item)
  return render_to_response('item/update.html', {'form': form}, context_instance=RequestContext(request))

@staff_only
@json_response
def delete(request, id = -1):
  return { 'route': request.path }
