# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 23:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20170107_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 8, 23, 58, 52, 482343)),
        ),
        migrations.AlterField(
            model_name='lease',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 22, 23, 58, 52, 483037)),
        ),
        migrations.AlterField(
            model_name='lease',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 8, 23, 58, 52, 483010)),
        ),
    ]
