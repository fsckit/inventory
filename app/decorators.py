import json
from django.http import HttpResponse

def json_response(fn):
  def wrapped(*args, **kwargs):
    response = json.dumps(fn(*args, **kwargs))
    return HttpResponse(response, mimetype='application/json')
  return wrapped




from django.contrib.auth.decorators import user_passes_test

staff_only = user_passes_test(lambda user:
    user.is_authenticated() and user.is_staff, login_url='/staff/login')

superuser_only = user_passes_test(lambda user:
    user.is_authenticated() and user.is_admin, login_url='/staff/login')
