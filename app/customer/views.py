from app.decorators import json_response, staff_only
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from app.customer.forms import CreateForm
from app.customer.models import Customer

@staff_only
def index(request):
  customer = Customer.objects.all().order_by('last_name')
  return render_to_response('customer/index.html', {'customer': customer}, context_instance=RequestContext(request))

@staff_only
@json_response('POST')
def create(request):
  if request.method == 'POST':
    form = CreateForm(request.POST, request.FILES)
    if form.is_valid():
      obj = form.save()
      return { 'success': True }
    return { 'success': False }
  else:
    form = CreateForm()
  return render_to_response('customer/create.html', {'form': form}, context_instance=RequestContext(request))

@staff_only
def read(request, id=-1):
  customer = Customer.objects.get(student_id=id)
  return render_to_response('customer/read.html', {'customer': customer}, context_instance=RequestContext(request))

@staff_only
@json_response('POST')
def update(request, id=-1):
  customer = Customer.objects.get(student_id=id)
  if request.method == 'POST':
    form = CreateForm(request.POST, request.FILES, instance=customer)
    if form.is_valid():
      obj = form.save()
      return { 'success': True }
    return { 'success': False }
  else:
    form = CreateForm(instance=customer)
  return render_to_response('customer/update.html', {'form': form}, context_instance=RequestContext(request))

@json_response
def delete(request, id = -1):
  return { 'route': request.path }
