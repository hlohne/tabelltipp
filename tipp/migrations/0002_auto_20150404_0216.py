# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tipp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lag',
            options={'ordering': ['-poeng', 'kamper_spilt', 'navn'], 'verbose_name_plural': 'lag'},
        ),
    ]
