from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    email = models.CharField(max_length=200, unique = True, blank = True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=200)
    event_name = models.CharField(max_length=200, blank = True)

    def __str__(self):
        return self.number

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_prize = models.CharField(max_length=100)
    event_winner = models.CharField(max_length=200, blank=True)
    start_time =  models.DateTimeField( blank=True)
    end_time =  models.DateTimeField( blank=True)

    def __str__(self):
        return self.event_name


