from django.db import models
from api.models import Session

class Person(models.Model):

    full_name = models.CharField(max_length=63, blank=True)
    bio = models.CharField(max_length=63, blank=True)
    company = models.CharField(max_length=63, blank=True)
    image_loc = models.CharField(max_length=63, blank=True)
    session = models.ManyToManyField(Session)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
