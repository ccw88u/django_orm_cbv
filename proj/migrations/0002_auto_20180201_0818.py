# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('tel', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('age', models.PositiveIntegerField()),
                ('member', models.ForeignKey(related_name='members', to='proj.company')),
            ],
        ),
        migrations.AlterField(
            model_name='reguser',
            name='addr',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='website',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
