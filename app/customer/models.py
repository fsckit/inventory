from django.db import models

class Customer(models.Model):
  # RIN for student lending or borrowing
  student_id   = models.IntegerField(unique=True)
  # Student's name split for better search functionality
  first_name   = models.CharField(max_length = 50)
  last_name    = models.CharField(max_length = 50)
  # Student's email for sending receipts
  email        = models.EmailField(max_length = 75)
  # Phone number for additional contact if necessary
  phone_number = models.CharField(max_length = 12)
  
  # .full_name property based on first/last name
  def _get_full_name(self):
    return '%s %s' % (self.first_name, self.last_name)
  full_name = property(_get_full_name)

  # String representation of student
  def __str__(self):
    return str(self.full_name)
