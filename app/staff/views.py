from app.decorators.json_response import *
from django.contrib.auth import authenticate, login
# All views still stubs.

@json_response
def login(request):
	return { 'route': request.path }

@json_response
def logout(request, id=-1):
	return { 'route': request.path }

@json_response
def changepwd(request, id=-1):
	return { 'route': request.path }

@json_response
def userinfo(request, id=-1):
	return { 'route': request.path }
