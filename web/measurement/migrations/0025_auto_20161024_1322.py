# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-24 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0024_auto_20161024_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traceroutemeasurement12',
            name='countries',
            field=models.ManyToManyField(through='measurement.Relation12', to='measurement.Countries'),
        ),
    ]
