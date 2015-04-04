# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tipp', '0003_auto_20150404_0846'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lag',
            options={'ordering': ['-poeng', '-maalforskjell', '-scoretemaal', 'kamper_spilt', 'navn'], 'verbose_name_plural': 'lag'},
        ),
    ]
