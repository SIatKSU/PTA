# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pta', '0005_auto_20170724_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='classinfo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]