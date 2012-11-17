from app.decorators import json_response, staff_only
from app.transaction.forms import TransactionForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from app.transaction.models import Transaction
# Brandon's Changes for email recpeits
from app.transaction.email import SendMessage
from uuid import uuid1 as guid

@staff_only
@json_response('POST')
def create(request):
  if request.method == 'POST':
    form = TransactionForm(request.POST, request.FILES)

    if form.is_valid():
      # TODO: Verify current state

      # Changes for Email
      form.instance.id = guid().hex
      instance = form.save()

      # Call SendMessage in email module
      SendMessage(instance)

      # Back to you
      
      return { 'success': True }
    return { 'success': False }
  else:
    form = TransactionForm()
    return render_to_response('transaction/create.html', {'form': form}, context_instance=RequestContext(request))

@staff_only
def read(request, id = -1):
  qs = Transaction.objects.get(pk=id)
  return render_to_response('transaction/read.html', {'o': qs}, context_instance=RequestContext(request))

@staff_only
@json_response
def update(request, id = -1):
  return { 'route': request.path }

@staff_only
@json_response
def delete(request, id = -1):
  return { 'route': request.path }
