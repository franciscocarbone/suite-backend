# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 17:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='escuela',
            name='director',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='escuela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contactos', to='escuelas.Escuela'),
        ),
    ]