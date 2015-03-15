# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='latitude',
            field=models.DecimalField(max_digits=20, decimal_places=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='status',
            name='longitude',
            field=models.DecimalField(max_digits=20, decimal_places=15),
            preserve_default=True,
        ),
    ]
