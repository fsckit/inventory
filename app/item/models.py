from django.db import models

class Item(models.model):
  name         = models.CharField(max_length = 100)
  label_id     = models.IntegerField()
  type         = models.CharField(max_length = 20)  
  
