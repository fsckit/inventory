from django.contrib.auth.views import login
from django.shortcuts import render_to_response
from django.template import RequestContext
from app.decorators import staff_only

def index(request):
  # Do a test here to see if we should display a login page or the stage
  if request.user.is_authenticated():
    return render_to_response('index.html', context_instance=RequestContext(request))
  else:
    # Use django's login, but we can use a custom template here
    return login(request, template_name='registration/login.html')
