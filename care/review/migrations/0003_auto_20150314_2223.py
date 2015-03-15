# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20150314_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 14, 22, 22, 53, 390287, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 14, 22, 22, 57, 992277, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
