# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0002_auto_20150328_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('score', models.DecimalField(max_digits=2, decimal_places=1)),
                ('rated_model', models.ForeignKey(to='myproject.RatedModel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RatedObject',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('publish_date', models.DateField(max_length=200)),
                ('rated_model', models.ForeignKey(to='myproject.RatedModel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
