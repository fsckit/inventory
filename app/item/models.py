from django.db import models
from app.customer.models import Customer

class Item(models.model):
  name         = models.CharField(max_length = 100)
  label_id     = models.IntegerField()
  owning_customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
  type         = models.CharField(max_length = 20)  
  
