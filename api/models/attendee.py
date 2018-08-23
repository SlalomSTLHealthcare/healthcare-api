from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import Session

class Attendee(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    company = models.CharField(max_length=63, blank=True)
    position = models.CharField(max_length=63, blank=True)
    twitter = models.CharField(max_length=63, blank=True)
    lunch = models.BooleanField(blank=True, default=True)
    diet = ArrayField(models.CharField(max_length=63, blank=True) ,size=4)
    diet_allergy = models.CharField(max_length=255, blank=True)
    tshirt_size = models.CharField(max_length=63, blank=True)
    comment = models.CharField(max_length=255, blank=True)
    session = models.ManyToManyField(Session, through='Session_Attendee')
    donate = models.BooleanField(blank=True, default=True)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

#, company="test", position="important", twitter="stuff",, tshirt_size='xl', comment="this is a comment",
class Session_Attendee(models.Model):
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    date_signedup =  models.DateTimeField(blank=True, null=True)
    session_max_capacity = models.PositiveSmallIntegerField(blank=True, null=True)
    session_tag= models.PositiveSmallIntegerField(blank=True, null=True)

@receiver(post_save, sender=User)
def create_user_attendee(sender, instance, created, **kwargs):
    if created:
        Attendee.objects.create(user=instance, diet=[])

@receiver(post_save, sender=User)
def save_user_attendee(sender, instance, **kwargs):
    instance.attendee.save()
