from django.core import serializers

def json_response(fn):
  def wrapped(*args, **kwargs):
    response = fn(*args, **kwargs)
    json = serializers.serialize('json', data)
    return HttpResponse(json, mimetype='application/json')
  return fn
