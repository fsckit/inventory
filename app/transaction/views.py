from app.decorators import json_response
from app.transaction.forms import TransactionForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from app.transaction.models import Transaction

def create(request):
  if request.method == 'POST':
    form = TransactionForm(request.POST, request.FILES)

    if form.is_valid():
      # TODO: Verify current state
      form.save()
      return HttpResponseRedirect(reverse('transaction_create'))
  else:
    form = TransactionForm()
    return render_to_response('transaction/transaction_create.html', {'form': form}, context_instance=RequestContext(request))

def read(request, id = -1):
  qs = Transaction.objects.get(pk=id)
  return render_to_response('transaction/transaction_read.html', {'o': qs}, context_instance=RequestContext(request))

@json_response
def update(request, id = -1):
  return { 'route': request.path }

@json_response
def delete(request, id = -1):
  return { 'route': request.path }
