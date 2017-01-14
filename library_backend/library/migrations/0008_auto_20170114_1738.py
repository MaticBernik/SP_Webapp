# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 16:38
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0007_auto_20170110_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Users_Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Message')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 14, 17, 38, 25, 476522)),
        ),
        migrations.AlterField(
            model_name='lease',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 28, 17, 38, 25, 477266)),
        ),
        migrations.AlterField(
            model_name='lease',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 14, 17, 38, 25, 477239)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 28, 17, 38, 25, 477815)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 14, 17, 38, 25, 477791)),
        ),
    ]
