# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-04 15:43
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('LCG', '0002_auto_20181204_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='checked',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]