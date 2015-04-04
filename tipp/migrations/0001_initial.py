# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('navn', models.CharField(max_length=128, unique=True)),
                ('poeng', models.IntegerField(default=0)),
                ('kamper_spilt', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-poeng', 'kamper_spilt'],
                'verbose_name_plural': 'lag',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Liga',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('navn', models.CharField(max_length=128, unique=True)),
                ('public', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PoengRegel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('navn', models.CharField(max_length=128, unique=True)),
                ('kortnavn', models.CharField(max_length=20, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tabell',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('navn', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tabelltipp',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('poeng', models.IntegerField(default=0)),
                ('liga', models.ForeignKey(null=True, to='tipp.Liga')),
            ],
            options={
                'ordering': ['-poeng'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TippetPlassering',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('tippet_plassering', models.IntegerField()),
                ('lag', models.ForeignKey(null=True, to='tipp.Lag')),
                ('tabelltipp', models.ForeignKey(null=True, to='tipp.Tabelltipp')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tabelltipp',
            name='plassertlag',
            field=models.ManyToManyField(through='tipp.TippetPlassering', to='tipp.Lag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tabelltipp',
            name='user',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='liga',
            name='deltakere',
            field=models.ManyToManyField(through='tipp.Tabelltipp', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='liga',
            name='poengregel',
            field=models.ForeignKey(to='tipp.PoengRegel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='liga',
            name='tabell',
            field=models.ForeignKey(to='tipp.Tabell'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lag',
            name='tabell',
            field=models.ForeignKey(to='tipp.Tabell'),
            preserve_default=True,
        ),
    ]
