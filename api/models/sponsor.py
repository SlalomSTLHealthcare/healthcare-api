from django.db import models

class Sponsor(models.Model):

    title = models.CharField(max_length=63, blank=True)
    name = models.CharField(max_length=63, blank=True)
    image_loc = models.CharField(max_length=63, blank=True)
    description = models.CharField(max_length=255, blank=True)
    sponsor_level = models.CharField(max_length=63, blank=True)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
