from django.db import models
from django.db.models.fields import CharField
from django.contrib.postgres.fields import ArrayField
from datetime import datetime
# Create your models here.


class Feed(models.Model):
    user = models.CharField(max_length=1000)
    date = models.DateField(default=datetime.now, blank=True)
    feed = models.CharField(max_length=10000)
    like = models.IntegerField()
    
class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    user = models.CharField(max_length=1000)
    message = models.CharField(max_length=10000)
    date = models.DateField(default=datetime.now, blank=True)
    roomid = models.CharField(max_length=1000)
