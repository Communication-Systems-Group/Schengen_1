# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0005_auto_20160801_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='stop_time',
            field=models.DateField(null=True),
        ),
    ]