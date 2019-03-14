# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-02 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_group', to='otree.Session')),
            ],
            options={
                'db_table': 'survey_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('age', otree.db.models.IntegerField(null=True, verbose_name='What is your age?')),
                ('gender', otree.db.models.StringField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10000, null=True, verbose_name='What is your gender?')),
                ('crt_bat', otree.db.models.IntegerField(null=True, verbose_name='\n        A bat and a ball cost 22 dollars in total.\n        The bat costs 20 dollars more than the ball.\n        How many dollars does the ball cost?')),
                ('crt_widget', otree.db.models.IntegerField(null=True, verbose_name='\n        "If it takes 5 machines 5 minutes to make 5 widgets,\n        how many minutes would it take 100 machines to make 100 widgets?"\n        ')),
                ('crt_lake', otree.db.models.IntegerField(null=True, verbose_name='\n        In a lake, there is a patch of lily pads.\n        Every day, the patch doubles in size.\n        If it takes 48 days for the patch to cover the entire lake,\n        how many days would it take for the patch to cover half of the lake?\n        ')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_player', to='otree.Session')),
            ],
            options={
                'db_table': 'survey_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'survey_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Subsession'),
        ),
    ]
