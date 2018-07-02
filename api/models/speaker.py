from django.db import models


class Speaker(models.Model):
    name = models.CharField(max_length=63, blank=True)
    company = models.CharField(max_length=63, blank=True)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
