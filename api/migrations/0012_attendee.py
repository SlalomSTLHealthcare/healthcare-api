# Generated by Django 2.0.7 on 2018-07-16 20:18

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20180711_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=63)),
                ('position', models.CharField(blank=True, max_length=63)),
                ('twitter', models.CharField(blank=True, max_length=63)),
                ('lunch', models.BooleanField()),
                ('diet', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=4)),
                ('diet_allergy', models.CharField(blank=True, max_length=255)),
                ('tshirt_size', models.CharField(blank=True, max_length=63)),
                ('comment', models.CharField(blank=True, max_length=255)),
                ('breakout_one', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(blank=True, null=True), size=10)),
                ('breakout_two', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(blank=True, null=True), size=10)),
                ('donate', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
