from django.db import models

class Customer(models.Model):
  full_name    = models.CharField(max_length = 50)
  email        = models.EmailField(max_length = 75)
  student_id   = models.IntegerField(unique=True)
  phone_number = models.CharField(max_length = 12)
  
  def __str__(self):
    return str(self.full_name)
