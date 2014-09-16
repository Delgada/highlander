# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20140916_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityentry',
            name='score',
            field=models.DecimalField(default=0, max_digits=15, decimal_places=8),
        ),
    ]
