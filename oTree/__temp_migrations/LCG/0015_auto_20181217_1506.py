# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-17 14:06
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('LCG', '0014_auto_20181207_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='cumulative_payoff',
            field=otree.db.models.FloatField(null=True),
        ),
    ]