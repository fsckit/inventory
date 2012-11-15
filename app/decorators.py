import json
from django.http import HttpResponse

# Accepts a method and only returns json on those types
def json_response(method):
  def decorator(fn):
    def wrapped(request, *args, **kwargs):
      if request.method == method:
        response = json.dumps(fn(request, *args, **kwargs))
        return HttpResponse(response, mimetype='application/json')
      else:
        return  fn(request, *args, **kwargs)
    return wrapped
  return decorator



from django.contrib.auth.decorators import user_passes_test

staff_only = user_passes_test(lambda user:
    user.is_authenticated() and user.is_staff, login_url='/staff/login')

superuser_only = user_passes_test(lambda user:
    user.is_authenticated() and user.is_admin, login_url='/staff/login')
