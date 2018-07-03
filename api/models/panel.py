from django.db import models
from django.contrib.postgres.fields import ArrayField

class Panel(models.Model):

    title = models.CharField(max_length=63, blank=True)
    panelists = ArrayField(models.CharField(max_length=63, blank=True))
    imageLoc = models.CharField(max_length=63, blank=True)
    description = models.CharField(max_length=255, blank=True)
    panel = models.PositiveSmallIntegerField(blank=True)


    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
