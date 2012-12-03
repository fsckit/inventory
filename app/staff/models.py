from django.contrib.auth.models import User
from django.db.models import Max
from app.transaction.models import Transaction

# Using django auth user -- this proxy model is only for methods
class Staff(User):
  def last_action(self):
    return Transaction.objects.filter(signoff=self).aggregate(Max('date'))['date__max']

  def num_actions(self):
    return Transaction.objects.filter(signoff=self).count()

  class Meta:
    proxy = True
