# Generated migration for Enfermeria group creation

from django.db import migrations
from django.contrib.auth.models import Group


def crear_grupo_enfermeria(apps, schema_editor):
    """Crear el grupo Enfermeria si no existe"""
    Group.objects.get_or_create(name='Enfermeria')


def eliminar_grupo_enfermeria(apps, schema_editor):
    """Eliminar el grupo Enfermeria"""
    try:
        grupo = Group.objects.get(name='Enfermeria')
        grupo.delete()
    except Group.DoesNotExist:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20251111_1811'),
    ]

    operations = [
        migrations.RunPython(crear_grupo_enfermeria, eliminar_grupo_enfermeria),
    ]
