from app.decorators.json_response import *

@json_response
def create(request):
  return { 'route': request.path }

@json_response
def read(request, id = -1):
  return { 'route': request.path }

@json_response
def update(request, id = -1):
  return { 'route': request.path }

@json_response
def delete(request, id = -1):
  return { 'route': request.path }
