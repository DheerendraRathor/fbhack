# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0004_auto_20150314_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 14, 22, 23, 1, 959566, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='status',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 14, 22, 23, 7, 332229, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
