import json
from django.http import HttpResponse

# Decorators wrap controllers to provide basic functional tests or transformations

# Accepts a method and only returns json on those types (e.g. 'POST')
def json_response(method):
  # Returns the decorator for the function
  def decorator(fn):
    def wrapped(request, *args, **kwargs):
      # The result of the controller is then passed here, and we dump it as a
      # JSON string if it matches the method
      if request.method == method:
        result = fn(request, *args, **kwargs)
        response = HttpResponse(json.dumps(result), mimetype='application/json')
        return response
      else:
        # Otherwise do the basic return 
        return fn(request, *args, **kwargs)
    return wrapped
  return decorator

# User test decorators
from django.contrib.auth.decorators import user_passes_test

# This controller is limited to staff only
staff_only = user_passes_test(lambda user:
    user.is_authenticated(), login_url='/staff/login')

# This controller is limited to superusers only
superuser_only = user_passes_test(lambda user:
    user.is_authenticated() and user.is_superuser, login_url='/staff/login')
