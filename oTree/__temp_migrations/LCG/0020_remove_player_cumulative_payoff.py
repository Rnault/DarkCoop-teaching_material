# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-18 09:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LCG', '0019_auto_20181218_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='cumulative_payoff',
        ),
    ]
