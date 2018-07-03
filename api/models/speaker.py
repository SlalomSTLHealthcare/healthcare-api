from django.db import models


class Speaker(models.Model):

    fullName = models.CharField(max_length=63, blank=True)
    title = models.CharField(max_length=63, blank=True)
    company = models.CharField(max_length=63, blank=True)
    imageLoc = models.CharField(max_length=63, blank=True)
    time = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
