# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 00:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20170108_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 9, 0, 1, 48, 983199)),
        ),
        migrations.AlterField(
            model_name='lease',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 23, 0, 1, 48, 983916)),
        ),
        migrations.AlterField(
            model_name='lease',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 9, 0, 1, 48, 983889)),
        ),
    ]
