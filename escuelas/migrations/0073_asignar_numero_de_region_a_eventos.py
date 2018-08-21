# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-08-20 17:46
from __future__ import unicode_literals
import progressbar

from django.db import migrations
from escuelas.models import Evento

def asignar_numero_de_region(apps, schema_editor):
    print("")
    print("Asignando numeros de region a los eventos")

    bar = progressbar.ProgressBar()
    eventos = Evento.objects.all()

    for evento in bar(eventos):
        evento.save()


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0072_auto_20180820_1740'),
    ]

    operations = [
        migrations.RunPython(asignar_numero_de_region, migrations.RunPython.noop),
    ]
