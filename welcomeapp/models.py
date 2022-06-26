from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Homes(models.Model):
    place = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.CharField(max_length=300)
