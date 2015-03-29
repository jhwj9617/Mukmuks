# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribute',
            name='rated_model',
        ),
        migrations.DeleteModel(
            name='Attribute',
        ),
        migrations.RemoveField(
            model_name='ratedobject',
            name='rated_model',
        ),
        migrations.DeleteModel(
            name='RatedObject',
        ),
    ]
