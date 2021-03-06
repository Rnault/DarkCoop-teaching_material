# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-02-01 14:39
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('LCG', '0055_auto_20190201_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='Dq1',
            field=otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Betting a day’s income at the horse races.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='Dq2',
            field=otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Investing 10% of your annual income in a moderate growth mutual fund.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='Dq3',
            field=otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Betting a day’s income at a high-stake poker game.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='Dq4',
            field=otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Investing 5% of your annual income in a very speculative stock.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='Dq5',
            field=otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Betting a day’s income on the outcome of a sporting event.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='Dq6',
            field=otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Investing 10% of your annual income in a new business venture.'),
        ),
    ]
