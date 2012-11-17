from django.contrib.auth.models import User
from django.db import models
from app.customer.models import Customer
from app.item.models import Item

class Transaction(models.Model):
  # Types for enumeration of items. We use a single character to identify it
  # because it helps for database readability and does not take up more space
  # than an integer.
  ACTIONS = (
    (u'b',	u'Borrow'), # Lend from the con to customer
    (u'l',	u'Lend'),   # Lend from item.owner to the con
    (u'r',	u'Return'), # Return from customer to the con
    (u'c',	u'Claim'),  # Return from the con to item.owner
  )


  id        = models.CharField(max_length=128, primary_key=True)
  # Date of transaction, handled automatically
  date      = models.DateTimeField(auto_now=True)
  # Action type as enumeration of above
  action    = models.CharField(max_length=2, choices=ACTIONS)
  # Customer, related item, and the staff member that signed off (generated the
  # transaction)
  customer  = models.ForeignKey(Customer, on_delete=models.PROTECT)
  item      = models.ForeignKey(Item, on_delete=models.PROTECT)
  signoff   = models.ForeignKey(User, on_delete=models.PROTECT)

