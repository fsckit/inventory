from django.db import models
from django.contrib.auth.models import User 

class Staff(models.User):
	# first_name, last_name, email are conveniently part of User, so nothing to do here
