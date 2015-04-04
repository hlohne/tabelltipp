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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navn', models.CharField(unique=True, max_length=128)),
                ('poeng', models.IntegerField(default=0)),
                ('kamper_spilt', models.IntegerField(default=0)),
                ('maalforskjell', models.IntegerField(default=0)),
                ('scoretemaal', models.IntegerField(default=0)),
                ('sorteringsnavn', models.CharField(max_length=128, null=True)),
            ],
            options={
                'ordering': ['-poeng', '-maalforskjell', '-scoretemaal', 'kamper_spilt', 'sorteringsnavn'],
                'verbose_name_plural': 'lag',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Liga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navn', models.CharField(unique=True, max_length=128)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navn', models.CharField(unique=True, max_length=128)),
                ('kortnavn', models.CharField(unique=True, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tabell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navn', models.CharField(unique=True, max_length=128)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tabelltipp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poeng', models.IntegerField(default=0)),
                ('liga', models.ForeignKey(to='tipp.Liga', null=True)),
            ],
            options={
                'ordering': ['-poeng'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TippetPlassering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tippet_plassering', models.IntegerField()),
                ('lag', models.ForeignKey(to='tipp.Lag', null=True)),
                ('tabelltipp', models.ForeignKey(to='tipp.Tabelltipp', null=True)),
            ],
            options={
                'ordering': ['tippet_plassering'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tabelltipp',
            name='plassertlag',
            field=models.ManyToManyField(to='tipp.Lag', through='tipp.TippetPlassering'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tabelltipp',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='liga',
            name='deltakere',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='tipp.Tabelltipp'),
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
