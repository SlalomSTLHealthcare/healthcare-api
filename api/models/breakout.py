from django.db import models


class Breakout(models.Model):

    title = models.CharField(max_length=63, blank=True)
    roomNum = models.CharField(max_length=63, blank=True)
    imageLoc = models.CharField(max_length=63, blank=True)
    time = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
