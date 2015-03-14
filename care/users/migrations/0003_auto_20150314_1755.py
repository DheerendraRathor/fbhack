# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150314_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='social_id',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
