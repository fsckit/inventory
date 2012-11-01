from django.db import models
from app.customer.models import Customer

class Item(models.Model):
  TYPES = (
    (u'g', u'game'),
    (u'c', u'console'),
    (u'n', u'controller'),
    (u'p', u'peripheral'),
    (u'o', u'other'),
  )

  # Id given to the physical item
  label_id = models.CharField(max_length = 20)
  # Brief description of the item
  name     = models.CharField(max_length = 100)
  # Person who lent the item to Genericon
  owner    = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
  # General type of the item
  type     = models.CharField(max_length = 20, choices=TYPES)
  
  def __str__(self):
    return str(self.name)
