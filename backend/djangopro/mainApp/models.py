from django.db import models
import datetime
# Create your models here.

class testnowtime(models.Model):
    idx = models.CharField(max_length=3,primary_key=True)
    con = models.TextField(null=True,default='')
