# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
        ('users', '0002_auto_20150314_1213'),
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.ForeignKey(to='status.Status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(to='users.Users'),
            preserve_default=True,
        ),
    ]
