# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-19 17:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0035_auto_20170919_1605'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evento',
            options={'ordering': ('-fecha',), 'verbose_name_plural': 'eventos'},
        ),
    ]
