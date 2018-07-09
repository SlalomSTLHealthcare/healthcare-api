from django.db import models

class Schedule(models.Model):

    title = models.CharField(max_length=63, blank=True)
    time = models.DateTimeField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

