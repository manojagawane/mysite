# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-20 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distributors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('latitude', models.FloatField(max_length=256)),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('latitude', models.FloatField(max_length=256)),
                ('longitude', models.FloatField()),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop', to='landing.Distributors')),
            ],
        ),
    ]