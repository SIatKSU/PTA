# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 21:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pta', '0002_auto_20170724_1711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homework',
            options={'ordering': ['-date_assigned'], 'verbose_name_plural': 'Homework'},
        ),
    ]
