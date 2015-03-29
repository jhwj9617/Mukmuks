# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0004_delete_penis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribute',
            name='rated_model',
        ),
        migrations.RemoveField(
            model_name='ratedobject',
            name='rated_model',
        ),
    ]
