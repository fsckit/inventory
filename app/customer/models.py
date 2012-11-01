from django.db import models

class Customer(models.Model):
  student_id   = models.IntegerField(primary_key=True)
  full_name    = models.CharField(max_length = 50)
  email        = models.EmailField(max_length = 75)
  phone_number = models.CharField(max_length = 12)
  
  def __str__(self):
    return str(self.full_name)
