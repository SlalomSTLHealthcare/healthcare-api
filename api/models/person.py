from django.db import models
from api.models import Session


class Person(models.Model):

    full_name = models.CharField(max_length=63, blank=True)
    title = models.CharField(max_length=255, blank=True)
    bio = models.CharField(max_length=1023, blank=True)
    company = models.CharField(max_length=63, blank=True)
    image_loc = models.CharField(max_length=255, blank=True)
    session = models.ManyToManyField(Session, blank=True)
    twitter = models.CharField(max_length=63, blank=True)
    linkedin = models.CharField(max_length=63, blank=True)
    hidden = models.BooleanField(blank=False, default=True)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
