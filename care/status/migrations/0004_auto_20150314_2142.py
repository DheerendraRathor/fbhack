# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import status.models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0003_status_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='image',
            field=models.ImageField(null=True, upload_to=status.models.get_filename),
            preserve_default=True,
        ),
    ]
