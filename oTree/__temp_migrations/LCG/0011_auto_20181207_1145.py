# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-07 10:45
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('LCG', '0010_auto_20181206_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='ingame',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True),
        ),
    ]
