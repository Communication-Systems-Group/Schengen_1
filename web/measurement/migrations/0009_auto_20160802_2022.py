# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0008_auto_20160802_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='target',
            field=models.CharField(max_length=100),
        ),
    ]