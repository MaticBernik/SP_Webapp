# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 18:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20170114_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 14, 19, 24, 44, 43806)),
        ),
        migrations.AlterField(
            model_name='lease',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 28, 19, 24, 44, 44502)),
        ),
        migrations.AlterField(
            model_name='lease',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 14, 19, 24, 44, 44475)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 28, 19, 24, 44, 45055)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 14, 19, 24, 44, 45032)),
        ),
    ]
