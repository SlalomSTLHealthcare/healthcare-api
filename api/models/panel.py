from django.db import models


class Panel(models.Model):

    title = models.CharField(max_length=63, blank=True)
    panelists = models.ArrayField(CharField(max_length=63, blank=True), size = 15)
    imageLoc = models.CharField(max_length=63, blank=True)
    description = models.CharField(max_length=255, blank=True)
    panel = models.PositiveSmallIntegerField(blank=True)


    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
