# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-01 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0002_auto_20170727_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='legacy_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
