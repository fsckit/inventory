from django.db import models

class Customer(models.Model):
  student_id   = models.IntegerField(primary_key=True)
  first_name   = models.CharField(max_length = 50)
  last_name    = models.CharField(max_length = 50)
  email        = models.EmailField(max_length = 75)
  phone_number = models.CharField(max_length = 12)
  
  
  def _get_full_name(self):
    return '%s %s' % (self.first_name, self.last_name)
  full_name = property(_get_full_name)

  def __str__(self):
    return str(self.full_name)
