from django.db import models
from app.customer.models import Customer

class Item(models.Model):
  # Types for enumeration of items. We use a single character to identify it
  # because it helps for database readability and does not take up more space
  # than an integer.
  TYPES = (
    (u'g', u'Game'),
    (u'c', u'Console'),
    (u'n', u'Controller'),
    (u'p', u'Peripheral'),
    (u'o', u'Other'),
  )

  # Id given to the physical item
  label_id = models.CharField(max_length = 20)
  # Brief description of the item
  name     = models.CharField(max_length = 100)
  # Person who lent the item to Genericon
  owner    = models.ForeignKey(Customer, on_delete=models.PROTECT)
  # General type of the item
  type     = models.CharField(max_length = 1, choices=TYPES)
  
  # Return an item instance as a string
  def __str__(self):
    return str(self.name)
