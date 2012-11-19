import re
import urllib
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import RequestContext
from app.decorators import json_response
from app.search.forms import SearchForm
from app.item.models import Item
from app.customer.models import Customer

# Helper method that splits a query string into search terms
def query_terms(qstr):
  return [filter(None, x)[0] for x in re.compile('"([^"]+)"|(\S+)').findall(qstr)]

# Handles the actual search
@json_response('GET', lambda r: 't' in r.GET and r.GET['t'] == 'json')
def search(request):
  form = SearchForm(request.GET, request.FILES)
  # Simple validation
  if form.is_valid():
    # Break down query terms
    qterms = query_terms(form.cleaned_data['q'])
    cq = None
    iq = None
    # Builds a complex database query based on search terms
    for term in qterms:
      # Customer fullname LIKE [any qterm]
      cq_inc = Q(last_name__icontains=term) | Q(first_name__icontains=term) | Q(email__icontains=term) | Q(student_id__icontains=term)
      # Item {name, owner} LIKE [any qterm] OR label = [any qterm]
      iq_inc = Q(name__icontains=term) | Q(label_id=term)
      if cq is None: # implies iq = None
        cq = cq_inc
        iq = iq_inc
      else: 
        cq = cq | cq_inc
        iq = iq | iq_inc
    # Fetches data from database for response
    customers = [{'key': customer.pk, 'id': customer.student_id, 'name': customer.full_name, 'extra': customer.email} for customer in Customer.objects.filter(cq)]
    items = [{'key': item.pk, 'id': item.label_id, 'name': item.name, 'extra': item.type} for item in Item.objects.filter(iq)]
    context = {'items': items, 'customers': customers}
    if 't' in request.GET and request.GET['t'] == 'json':
      return context
    else:
      return render_to_response('search/results.html', context, context_instance=RequestContext(request))
  else:
    # Returns the form; will not be used aside from testing
    return render_to_response('search/search.html', {'form': form}, context_instance=RequestContext(request))
