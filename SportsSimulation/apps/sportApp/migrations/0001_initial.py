# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-18 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('year', models.IntegerField()),
                ('position', models.CharField(max_length=12)),
                ('ability', models.DecimalField(decimal_places=2, max_digits=5)),
                ('create_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team', models.IntegerField()),
                ('away_team', models.IntegerField()),
                ('home_score', models.IntegerField(blank=True, default=None, null=True)),
                ('away_score', models.IntegerField(blank=True, default=None, null=True)),
                ('result', models.IntegerField(blank=True, default=None, null=True)),
                ('week_num', models.IntegerField()),
                ('create_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=45)),
                ('city', models.CharField(max_length=45)),
                ('state', models.CharField(max_length=45)),
                ('ability', models.DecimalField(decimal_places=2, max_digits=5)),
                ('team_num', models.IntegerField()),
                ('create_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='players',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='sportApp.Team'),
        ),
    ]
