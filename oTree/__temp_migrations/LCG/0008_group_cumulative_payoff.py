# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-05 14:01
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('LCG', '0007_auto_20181205_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='cumulative_payoff',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
