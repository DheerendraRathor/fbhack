# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150314_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('comment', models.TextField()),
                ('rate', models.DecimalField(max_digits=3, decimal_places=1)),
                ('latitude', models.DecimalField(max_digits=12, decimal_places=8)),
                ('longitude', models.DecimalField(max_digits=12, decimal_places=8)),
                ('address', models.TextField()),
                ('user', models.ForeignKey(to='users.Users')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
