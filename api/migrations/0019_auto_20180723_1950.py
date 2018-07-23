# Generated by Django 2.0.7 on 2018-07-23 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_emailsignup_sponsorquery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
