# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-07 11:05
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('LCG', '0013_auto_20181207_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsession',
            name='ingame',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True),
        ),
    ]
