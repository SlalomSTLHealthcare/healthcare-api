# Generated by Django 2.0.7 on 2018-07-11 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20180711_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='image_loc',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
