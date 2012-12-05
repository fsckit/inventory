from socketio import socketio_manage
from django.contrib.auth.views import login
from django.shortcuts import render_to_response
from django.template import RequestContext
from app.decorators import staff_only
from app.item.forms import ItemCreate
from app.customer.forms import CreateForm
from app.transaction.forms import TransactionForm
from app.customer.models import Customer
from app.item.forms import Item
from app.comm import SubscribeNamespace

def index(request):
  # Do a test here to see if we should display a login page or the stage
  if request.user.is_authenticated():
    # Initial forms are pulled from their respective sub-application forms
    context = {
       "item_form":ItemCreate(),
       "customer_form":CreateForm(),
       "trans_form":TransactionForm(),
    }
    return render_to_response('stage.html', context, context_instance=RequestContext(request))
  else:
    # Use django's login, but we can use a custom template here
    return login(request, template_name='registration/login.html')

def subscribe(request):
  if 'socketio' not in request.environ:
    raise Exception('Socket.io functionality not available on server')
  socketio_manage(request.environ, {'/subscribe': SubscribeNamespace}, request)
