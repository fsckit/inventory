import json
from django.http import HttpResponse

def json_response(fn):
  def wrapped(*args, **kwargs):
    response = json.dumps(fn(*args, **kwargs))
    return HttpResponse(response, mimetype='application/json')
  return wrapped
