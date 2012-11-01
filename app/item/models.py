from django.db import models
from app.customer.models import Customer

class Item(models.Model):
  name         = models.CharField(max_length = 100)
  label_id     = models.IntegerField(unique=True)

  # Person who is currently holding the object in question
  owning_customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)

  # Name of the person who owns the object in question
  owner_name = models.CharField(max_length=100)
  type = models.CharField(max_length = 20)  
  
  def __str__(self):
    return str(self.name)
