# Generated by Django 2.0.7 on 2018-07-02 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='company',
            field=models.CharField(blank=True, max_length=63),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='name',
            field=models.CharField(blank=True, max_length=63),
        ),
    ]