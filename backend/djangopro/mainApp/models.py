from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=10,primary_key=True)
    taglist = models.TextField()
class Typelist(models.Model):
    name = models.CharField(max_length=10,primary_key=True)
class QuestionList(models.Model):
    que = models.CharField(max_length=30,primary_key=True)
    ans1 = models.CharField(max_length=20)
    ans2 = models.CharField(max_length=20)

#top 3

