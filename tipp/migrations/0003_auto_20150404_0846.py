# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tipp', '0002_auto_20150404_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='lag',
            name='maalforskjell',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lag',
            name='scoretemaal',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
