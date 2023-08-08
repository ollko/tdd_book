from django.db import models

# Create your models here.
class Item(models.Model):
    '''list item'''
    text = models.TextField(default='')