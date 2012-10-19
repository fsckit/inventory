from django.db import models

class Customer(models.model):
  full_name    = models.CharField(max_length = 50)
  email        = models.EmailField(max_length = 75)
  student_id   = models.IntegerField()
  phone_number = models.CharField(max_length = 12)
