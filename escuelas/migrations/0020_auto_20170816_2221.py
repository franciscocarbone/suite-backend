# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-16 22:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0019_escuela_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escuela',
            name='padre',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subescuelas', to='escuelas.Escuela'),
        ),
    ]
