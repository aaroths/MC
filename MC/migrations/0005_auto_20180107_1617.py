# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-01-07 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MC', '0004_auto_20180107_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='statementNumber',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default='1'),
        ),
    ]
