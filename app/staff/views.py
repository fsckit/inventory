from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.template import RequestContext
from app.decorators import json_response, staff_only
from app.staff.forms import CreateForm


@json_response
def read(request, id = -1):
	return { 'route': request.path }

# @staff_only
def create(request):
  if request.method == 'POST':
    form = CreateForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('staff_create'))
  else:
    form = CreateForm()

  return render_to_response('staff/create.html', {'form': form}, context_instance=RequestContext(request))
