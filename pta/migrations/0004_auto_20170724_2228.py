# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pta', '0003_auto_20170724_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='points',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
    ]
