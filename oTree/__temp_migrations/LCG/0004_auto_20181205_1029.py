# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-05 09:29
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('LCG', '0003_auto_20181204_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='p1_cheat',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='p2_cheat',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='team_cheated',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
