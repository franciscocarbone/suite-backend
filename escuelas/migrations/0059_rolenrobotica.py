# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-07-30 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0058_cargar_app_suite_a_usuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='RolEnRobotica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
            options={
                'db_table': 'roles_en_robotica',
                'verbose_name_plural': 'roles_en_robotica',
            },
        ),
    ]
