from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

class Attendee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=63, blank=True)
    position = models.CharField(max_length=63, blank=True)
    twitter = models.CharField(max_length=63, blank=True)
    lunch = models.BooleanField(blank=True)
    diet = ArrayField(models.CharField(max_length=10, blank=True),size=4)
    diet_allergy = models.CharField(max_length=255, blank=True)
    tshirt_size = models.CharField(max_length=63, blank=True)
    comment = models.CharField(max_length=255, blank=True)
    breakout_one = ArrayField(models.PositiveSmallIntegerField(blank=True, null=True),size=10)
    breakout_two = ArrayField(models.PositiveSmallIntegerField(blank=True, null=True),size=10)
    donate = models.BooleanField(blank=True)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
