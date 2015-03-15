# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_auto_20150314_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='image',
            field=models.ImageField(null=True, upload_to=b'get_filename'),
            preserve_default=True,
        ),
    ]
