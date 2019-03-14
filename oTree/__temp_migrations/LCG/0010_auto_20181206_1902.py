# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-06 18:02
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('LCG', '0009_auto_20181206_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='cumulative_payoff',
        ),
        migrations.AddField(
            model_name='player',
            name='cumulative_payoff',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]