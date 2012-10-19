from django.db import models

class Transaction(models.model):
  ACTIONS = (
    (u'b',	u'borrow'),
	(u'l',	u'lend'),
	(u'r',	u'return'),
	(u'c',	u'claim'),
  )
  date      = models.DateTime(auto_now=True)
  action    = models.CharField(max_leng=2, choices=ACTIONS)
