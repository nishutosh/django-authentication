from __future__ import unicode_literals

from django.db import models

class users(models.Model):
    username=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)
    is_active=models.BooleanField(default=True)
    

# Create your models here.
