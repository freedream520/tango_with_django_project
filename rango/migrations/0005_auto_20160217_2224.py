# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='first_visit',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 17, 22, 24, 39, 600682), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='last_visit',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 2, 17, 22, 24, 59, 159515)),
            preserve_default=False,
        ),
    ]
