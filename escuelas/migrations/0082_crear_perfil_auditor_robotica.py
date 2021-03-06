# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-11-26 14:11
from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations

def cargar_rol_de_auditor_y_permisos(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    ContentType = apps.get_model("contenttypes", "ContentType")
    Permission = apps.get_model("auth", "Permission")

    grupo = Group.objects.create(name="AuditorRobotica")

    tipo, _ = ContentType.objects.get_or_create(app_label='escuelas', model=grupo)
    permiso_generar_informes = Permission.objects.create(name="generar_informes",
        codename="perfil.generar_informes",
        content_type=tipo)

    # Asignar los permisos agenda.lista y generar informesla grupo "AuditorRobotica"
    try:
        permiso_listar_talleres =  Permission.objects.get(codename="agenda.listar")
        permiso_agenda_exportar =  Permission.objects.get(codename="agenda.exportar")

        grupo.permissions.add(permiso_listar_talleres)
        grupo.permissions.add(permiso_agenda_exportar)
    except ObjectDoesNotExist:
        print("Omitiendo vincular permisos que no existen.")

    grupo.permissions.add(permiso_generar_informes)

    # Asigna el permiso "perfil.generar_informes" a todos los grupos que tengan
    # "perfil.global".
    for grupo in Group.objects.all():
        if 'perfil.global' in [p.codename for p in grupo.permissions.all()]:
            grupo.permissions.add(permiso_generar_informes)


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0081_paquete_perfil_que_solicito_el_paquete'),
    ]

    operations = [
        migrations.RunPython(cargar_rol_de_auditor_y_permisos, migrations.RunPython.noop),
    ]
