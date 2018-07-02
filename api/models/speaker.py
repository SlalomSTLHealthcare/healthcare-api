from django.db import models


class Speaker(models.Model):
    '''
    Holds meta information about an Account, not used to login.
    '''
    name = models.CharField(max_length=63, blank=False)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
