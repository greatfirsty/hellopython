# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-27 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='u_age',
            field=models.IntegerField(default=18, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='user',
            name='u_name',
            field=models.CharField(max_length=16, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='u_score',
            field=models.IntegerField(default=60, verbose_name='分数'),
        ),
    ]