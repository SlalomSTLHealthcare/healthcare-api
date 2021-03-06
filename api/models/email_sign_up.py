from django.db import models


class EmailSignUp(models.Model):
    email = models.CharField(max_length=127)
    name = models.CharField(max_length=127, blank=True)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
