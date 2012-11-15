import re
import urllib

from app.search.forms import SearchForm
from app.item.models import Item
from app.customer.models import Customer
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import RequestContext

def query_terms(qstr):
  return [filter(None, x)[0] for x in re.compile('"([^"]+)"|(\S+)').findall(qstr)]

def search(request):
  form = SearchForm(request.GET, request.FILES)
  if form.is_valid():
    qterms = query_terms(form.cleaned_data['qstr'])
    cq = None
    iq = None
    for term in qterms:
      # Customer fullname LIKE [any qterm]
      cq_inc = Q(full_name__icontains=term) | Q(email__icontains=term)
      # Item {name, owner} LIKE [any qterm] OR label = [any qterm]
      iq_inc = Q(name__icontains=term) | Q(label_id=term)
      if cq is None: # implies iq = None
        cq = cq_inc
        iq = iq_inc
      else: 
        cq = cq | cq_inc
        iq = iq | iq_inc
    customers = [(customer.full_name, customer.email, customer.student_id) for customer in Customer.objects.filter(cq)]
    items = [(item.name, item.label_id, item.pk) for item in Item.objects.filter(iq)]
    return render_to_response('search/results.html', {'items': items, 'customers': customers}, context_instance=RequestContext(request))
  else:
    return render_to_response('search/search.html', {'form': form}, context_instance=RequestContext(request))
