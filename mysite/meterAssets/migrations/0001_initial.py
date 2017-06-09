# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-09 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(max_length=12)),
                ('badge_number', models.CharField(max_length=12)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
