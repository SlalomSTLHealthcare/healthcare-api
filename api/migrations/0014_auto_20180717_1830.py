# Generated by Django 2.0.7 on 2018-07-17 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_attendee_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='donate',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='lunch',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]