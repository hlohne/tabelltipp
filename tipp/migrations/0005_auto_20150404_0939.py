# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tipp', '0004_auto_20150404_0849'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lag',
            options={'verbose_name_plural': 'lag', 'ordering': ['-poeng', '-maalforskjell', '-scoretemaal', 'kamper_spilt', 'sorteringsnavn']},
        ),
        migrations.AddField(
            model_name='lag',
            name='sorteringsnavn',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
    ]
