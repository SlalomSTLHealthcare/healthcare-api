# Generated by Django 2.0.7 on 2018-08-24 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20180823_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='industry',
            field=models.CharField(blank=True, max_length=63),
        ),
    ]
