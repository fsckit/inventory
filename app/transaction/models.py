from django.contrib.auth.models import User
from django.db import models
from app.customer.models import Customer
from app.item.models import Item

class Transaction(models.Model):
  ACTIONS = (
    (u'b',	u'Borrow'), # Lend from the con to customer
    (u'l',	u'Lend'),   # Lend from item.owner to the con
    (u'r',	u'Return'), # Return from customer to the con
    (u'c',	u'Claim'),  # Return from the con to item.owner
  )

  date      = models.DateTimeField(auto_now=True)
  action    = models.CharField(max_length=2, choices=ACTIONS)
  customer  = models.ForeignKey(Customer, on_delete=models.PROTECT)
  item      = models.ForeignKey(Item, on_delete=models.PROTECT)
  signoff   = models.ForeignKey(User, on_delete=models.PROTECT)
