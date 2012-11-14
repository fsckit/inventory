import re

from app.search.forms import SearchForm
from app.item.models import Item
from app.customer.models import Customer
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import RequestContext

def query_terms(qstr):
  return [filter(None, x)[0] for x in re.compile('"([^"]+)"|(\S+)').findall(qstr)]



def search(request):
  if request.method == 'POST':
    form = SearchForm(request.POST, request.FILES)
    if form.is_valid():
      item_name_q = query_terms(form.cleaned_data['item_name'])

      iq = None
      for term in item_name_q:
        cq = Q(name__icontains=term)
        if iq is None:
          iq = cq
        else:
          iq = iq & cq
      lbl = form.cleaned_data['item_label']
      if lbl != '':
        cq = Q(label_id=lbl)
        if iq is None:
          iq = cq
        else:
          iq = iq & cq

      items = None
      if iq is not None:
        items = [(item.name, item.label_id, item.pk) for item in Item.objects.filter(iq)]

      cust_name_q = form.cleaned_data['cust_name']
      customers = None
      if cust_name_q != '':
        customers = [(customer.full_name, customer.email, customer.student_id) for customer in Customer.objects.filter(full_name__icontains=cust_name_q)]
      return render_to_response('search/results.html', {'items': items, 'customers': customers}, context_instance=RequestContext(request))
  else:
    form = SearchForm()
  return render_to_response('search/search.html', {'form': form}, context_instance=RequestContext(request))
