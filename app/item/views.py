from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from app.item.forms import ItemCreate
from app.item.models import Item
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def create(request):
  if request.method == 'POST':
    form = ItemCreate(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('item_read'))
  else:
    form = ItemCreate()
  return render_to_response('item/item_create.html', {'form': form}, context_instance=RequestContext(request))
 
def read(request, id = -1):
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
