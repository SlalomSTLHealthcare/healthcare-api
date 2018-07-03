# Generated by Django 2.0.7 on 2018-07-03 16:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180703_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=63)),
                ('panelists', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=63), size=None)),
                ('imageLoc', models.CharField(blank=True, max_length=63)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('panel', models.PositiveSmallIntegerField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
