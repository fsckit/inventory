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

def read(request, id=-1):
  customer = Customer.objects.get(student_id=id)
  return render_to_response('customer/customer_read.html', {'customer': customer}, context_instance=RequestContext(request))

def update(request, id=-1):
  customer = Customer.objects.get(student_id=id)
  if request.method == 'POST':
    form = CreateForm(request.POST, request.FILES, instance=customer)
    if form.is_valid():
      obj = form.save()
      return HttpResponseRedirect(reverse('customer_read', args=[obj.student_id]))
  else:
    form = CreateForm(instance=customer)
  return render_to_response('customer/customer_update.html', {'form': form}, context_instance=RequestContext(request))


@json_response
def delete(request, id = -1):
  return { 'route': request.path }
