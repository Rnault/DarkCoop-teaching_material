# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-21 09:02
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('LCG', '0050_auto_20190117_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='q11',
            field=otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6']], null=True, verbose_name='If no one is watching or will know, it does not matter if I do the right thing.'),
        ),
    ]
