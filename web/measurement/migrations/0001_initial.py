# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-31 21:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Probes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protocol', models.CharField(choices=[('ICMP', 'ICMP'), ('UDP', 'UDP'), ('TCP', 'TCP')], default='TCP', max_length=5)),
                ('one_off', models.BooleanField(default=False)),
                ('start_time', models.DateField(auto_now_add=True)),
                ('stop_time', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('probes', models.ManyToManyField(to='measurement.Probes')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.Specification')),
            ],
        ),
    ]
