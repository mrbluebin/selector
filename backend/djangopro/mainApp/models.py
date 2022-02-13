from django.db import models
import datetime
# Create your models here.

class testnowtime(models.Model):
    idx = models.CharField(max_length=40,default='')
    con = models.TextField(null=True,default='')
