# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0005_auto_20150329_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='rated_model',
            field=models.ForeignKey(to='myproject.RatedModel', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ratedobject',
            name='rated_model',
            field=models.ForeignKey(to='myproject.RatedModel', null=True),
            preserve_default=True,
        ),
    ]
