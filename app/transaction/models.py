import os
from django.contrib.auth.models import User
from django.db import models
from app import utils
from app.customer.models import Customer
from app.item.models import Item

class Transaction(models.Model):
  # Types for enumeration of items. We use a single character to identify it
  # because it helps for database readability and does not take up more space
  # than an integer.
  ACTIONS = (
    (u'b',	u'In Stock'), # Lend from the con to customer
    (u'l',	u'Out of Room'),   # Lend from item.owner to the con
    (u'r',	u'Returned to Room'), # Return from customer to the con
    (u'c',	u'Claimed by Owner'),  # Return from the con to item.owner
  )


  id        = models.IntegerField(primary_key=True)
  # Date of transaction, handled automatically
  date      = models.DateTimeField(auto_now=True)
  # Action type as enumeration of above
  action    = models.CharField(max_length=2, choices=ACTIONS)
  # Customer, related item, and the staff member that signed off (generated the
  # transaction)
  customer  = models.ForeignKey(Customer, on_delete=models.PROTECT)
  item      = models.ForeignKey(Item, on_delete=models.PROTECT)
  signoff   = models.ForeignKey(User, on_delete=models.PROTECT)

  def send_email(self):pass
#    CHOICES = {'b': 'borrow.html', 'l': 'lend.html', 'r': 'return.html', 'c': 'claim.html'}
#    template = os.path.join('email', CHOICES[self.action])
#
#    # Generate email
#    utils.mailer(
#      to = self.customer.email,
#      subject = 'Genericon Transaction Completed',
#      template = template,
#      context = {
#        'customer': self.customer,
#        'item': self.item,
#        'id': self.id,
#      }
#    )

