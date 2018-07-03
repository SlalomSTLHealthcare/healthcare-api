from django.db import models

class Session(models.Model):

    title = models.CharField(max_length=63, blank=True)
    session_type = models.CharField(max_length=63, blank=True)
    image_loc = models.CharField(max_length=63, blank=True)
    description = models.CharField(max_length=255, blank=True)
    time = models.DateTimeField(blank=True, null=True)
    room_num = models.PositiveSmallIntegerField(blank=True, null=True)


    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
