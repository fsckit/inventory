from app.decorators import json_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from app.customer.forms import TakeItemForm
from app.customer.forms import CreateForm
from app.customer.models import Customer

def create(request):
  if request.method == 'POST':
    form = CreateForm(request.POST, request.FILES)
    if form.is_valid():
      obj = form.save()
      return HttpResponseRedirect(reverse('customer_read', args=[obj.student_id]))
  else:
    form = CreateForm()
  return render_to_response('customer/customer_create.html', {'form': form}, context_instance=RequestContext(request))

def read(request, id = -1):
  customer = Customer.objects.get(student_id=id)
  return render_to_response('customer/customer_read.html', {'customer': customer}, context_instance=RequestContext(request))

def update(request, id = -1):
  if request.method == 'POST':
    # If user not logged in, redirect to login
    if not request.user.is_authenticated():
      return HttpResponseRedirect('/')

    form = CreateForm(request.POST, request.FILES)
    if form.is_valid():
      # TODO: This isn't exactly threadsafe
      qs = Item.objects.filter(owning_customer__isnull, id=form.item_id)

      # if qs is empty, then either the item does not exist or it's owned. 
      if len(qs) != 0:
        item = qs.pop()
        item.owning_customer = id
        item.save()
        # display success
      else:
	qs = qs # empty statement so there's no error
        # emit error to user
  else:
    form = TakeItemForm()
  return render_to_response('customer/update.html', {'form': form}, context_instance=RequestContext(request))


@json_response
def delete(request, id = -1):
  return { 'route': request.path }
