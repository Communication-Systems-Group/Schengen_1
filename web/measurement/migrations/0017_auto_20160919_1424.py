# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-19 14:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0016_auto_20160919_1314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='traceroute1',
            old_name='timestamp',
            new_name='timestamp1',
        ),
    ]
