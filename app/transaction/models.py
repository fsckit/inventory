from django.db import models
from app.customer.models import Customer
from app.item.models import Item

class Transaction(models.Model):
  ACTIONS = (
    (u'b',	u'borrow'), # Lend from the con to customer
    (u'l',	u'lend'),   # Lend from item.owner to the con
    (u'r',	u'return'), # Return from customer to the con
    (u'c',	u'claim'),  # Return from the con to item.owner
  )

  date      = models.DateTimeField(auto_now=True)
  action    = models.CharField(max_length=2, choices=ACTIONS)
  customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
  item = models.ForeignKey(Item, on_delete=models.PROTECT)
