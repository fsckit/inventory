from django.db import models

class Transaction(models.Model):
  ACTIONS = (
    (u'b',	u'borrow'),
	(u'l',	u'lend'),
	(u'r',	u'return'),
	(u'c',	u'claim'),
  )
  date      = models.DateTimeField(auto_now=True)
  action    = models.CharField(max_length=2, choices=ACTIONS)
