"""
Script para actualizar nombres de Usuarios con nombres más realistas
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from myapp.models import Identificacion

print("=" * 80)
print("ACTUALIZACIÓN DE NOMBRES DE Usuarios")
print("=" * 80)

# Definir nuevos nombres más realistas
actualizaciones = {
    2: {"primer_nombre": "Carmen", "segundo_nombre": "Rosa", "primer_apellido": "Rodríguez", "segundo_apellido": "García"},
    3: {"primer_nombre": "Luis", "segundo_nombre": "Alberto", "primer_apellido": "González", "segundo_apellido": "Méndez"},
    4: {"primer_nombre": "Patricia", "segundo_nombre": "Isabel", "primer_apellido": "Ramírez", "segundo_apellido": "Castro"},
    5: {"primer_nombre": "Carlos", "segundo_nombre": "Eduardo", "primer_apellido": "Hernández", "segundo_apellido": "Morales"},
    7: {"primer_nombre": "Sofía", "segundo_nombre": "Beatriz", "primer_apellido": "Torres", "segundo_apellido": "Jiménez"},
    8: {"primer_nombre": "Miguel", "segundo_nombre": "Ángel", "primer_apellido": "Martínez", "segundo_apellido": "López"},
}

print("\nActualizando Usuarios con nombres más realistas...\n")

for paciente_id, datos in actualizaciones.items():
    try:
        paciente = Identificacion.objects.get(id=paciente_id)
        nombre_anterior = f"{paciente.primer_nombre} {paciente.segundo_nombre} {paciente.primer_apellido} {paciente.segundo_apellido}"
        
        # Actualizar los datos
        paciente.primer_nombre = datos["primer_nombre"]
        paciente.segundo_nombre = datos["segundo_nombre"]
        paciente.primer_apellido = datos["primer_apellido"]
        paciente.segundo_apellido = datos["segundo_apellido"]
        paciente.save()
        
        nombre_nuevo = f"{paciente.primer_nombre} {paciente.segundo_nombre} {paciente.primer_apellido} {paciente.segundo_apellido}"
        
        print(f"✓ ID {paciente_id}:")
        print(f"  Anterior: {nombre_anterior}")
        print(f"  Nuevo:    {nombre_nuevo}")
        print()
        
    except Identificacion.DoesNotExist:
        print(f"✗ Paciente con ID {paciente_id} no encontrado")

print("=" * 80)
print("LISTADO ACTUALIZADO DE Usuarios")
print("=" * 80)

Usuarios = Identificacion.objects.all().order_by('id')
for paciente in Usuarios:
    nombre_completo = f"{paciente.primer_nombre} {paciente.segundo_nombre} {paciente.primer_apellido} {paciente.segundo_apellido}".strip()
    print(f"ID {paciente.id:2d}: {nombre_completo:45s} - {paciente.edad} años - {paciente.ciudad_residencia}")

print("\n✅ Actualización completada exitosamente!")
print("=" * 80)
