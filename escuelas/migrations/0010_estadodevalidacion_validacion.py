# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-04 18:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0009_auto_20170804_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoDeValidacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'estadosDeValidacion',
                'verbose_name_plural': 'estadosDeValidacion',
            },
        ),
        migrations.CreateModel(
            name='Validacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.IntegerField()),
                ('fechaDeAlta', models.DateField(blank=True, default=None, null=True)),
                ('cantidad', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('observaciones', models.TextField(max_length=1024)),
                ('autor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='validaciones', to='escuelas.Perfil')),
                ('escuela', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='validaciones', to='escuelas.Escuela')),
                ('estado', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='validaciones', to='escuelas.EstadoDeValidacion')),
            ],
            options={
                'db_table': 'validaciones',
                'verbose_name_plural': 'validaciones',
            },
        ),
    ]
