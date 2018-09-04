from django.db import models
from .schedule import Schedule

class Session(models.Model):

    title = models.CharField(max_length=63, blank=True)
    session_type = models.CharField(max_length=63, blank=True)
    image_loc = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=1023, blank=True)
    time = models.DateTimeField(blank=True, null=True)
    room_num = models.CharField(max_length=63, blank=True, null=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.PROTECT, related_name='sessions', null=True)
    max_capacity = models.PositiveSmallIntegerField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
