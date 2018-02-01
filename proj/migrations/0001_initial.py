# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reguser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('addr', models.CharField(max_length=191)),
                ('tel', models.CharField(max_length=128)),
                ('email', models.EmailField(unique=True, max_length=190)),
                ('profile_pic', models.ImageField(upload_to=b'profile_pics', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=191)),
                ('uri', models.URLField(blank=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='website_subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_name', models.CharField(unique=True, max_length=190)),
            ],
        ),
        migrations.AddField(
            model_name='website',
            name='subject',
            field=models.ForeignKey(to='proj.website_subject'),
        ),
    ]
