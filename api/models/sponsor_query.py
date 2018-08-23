from django.db import models


class SponsorQuery(models.Model):
    name = models.CharField(max_length=127, blank=True)
    email = models.CharField(max_length=127)
    company = models.CharField(max_length=127, blank=True, null=True)
    notes = models.CharField(max_length=1023, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
