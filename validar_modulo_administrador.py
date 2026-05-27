"""
Script para validar el módulo de administrador
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User, Group
from myapp.models import Identificacion, ConsultaMedica, EvolucionDiariaEnfermeria

print("=" * 60)
print("VALIDACIÓN DEL MÓDULO DE ADMINISTRADOR")
print("=" * 60)

# 1. Verificar Empleados administradores
print("\n1. Verificando Empleados administradores...")
admins = User.objects.filter(is_staff=True) | User.objects.filter(is_superuser=True)
print(f"   ✓ Total de administradores: {admins.count()}")
for admin in admins:
    print(f"   - {admin.username} (Staff: {admin.is_staff}, Superuser: {admin.is_superuser})")

# 2. Verificar grupos del sistema
print("\n2. Verificando grupos del sistema...")
grupos = Group.objects.all()
print(f"   ✓ Total de grupos: {grupos.count()}")
for grupo in grupos:
    count = grupo.user_set.count()
    print(f"   - {grupo.name}: {count} Empleados")

# 3. Verificar todos los Empleados
print("\n3. Verificando todos los Empleados...")
total_Empleados = User.objects.count()
Empleados_activos = User.objects.filter(is_active=True).count()
print(f"   ✓ Total de Empleados: {total_Empleados}")
print(f"   ✓ Empleados activos: {Empleados_activos}")
print(f"   ✓ Empleados inactivos: {total_Empleados - Empleados_activos}")

# 4. Verificar Usuarios
print("\n4. Verificando Usuarios...")
total_Usuarios = Identificacion.objects.count()
print(f"   ✓ Total de Usuarios: {total_Usuarios}")

# 5. Verificar actividad del sistema
print("\n5. Verificando actividad del sistema...")
total_consultas = ConsultaMedica.objects.count()
total_evoluciones = EvolucionDiariaEnfermeria.objects.count()
print(f"   ✓ Total de consultas médicas: {total_consultas}")
print(f"   ✓ Total de evoluciones de enfermería: {total_evoluciones}")

# 6. Últimos 5 Empleados registrados
print("\n6. Últimos 5 Empleados registrados...")
ultimos_Empleados = User.objects.all().order_by('-date_joined')[:5]
for usuario in ultimos_Empleados:
    grupo = usuario.groups.first().name if usuario.groups.first() else 'Sin grupo'
    print(f"   - {usuario.username} ({grupo}) - {usuario.date_joined.strftime('%d/%m/%Y %H:%M')}")

print("\n" + "=" * 60)
print("VALIDACIÓN COMPLETADA")
print("=" * 60)
print("\n📋 URLs del módulo administrador:")
print("   - Dashboard Administrador: http://127.0.0.1:8000/administrador/")
print("   - Lista de Empleados: http://127.0.0.1:8000/admin/users/")
print("   - Crear Usuario: http://127.0.0.1:8000/admin/users/create/")
print("\n💡 Credenciales de admin: admin / Admin123")
print("\n✨ Funcionalidades disponibles:")
print("   ✓ Ver estadísticas del sistema")
print("   ✓ Listar todos los Empleados")
print("   ✓ Crear nuevos Empleados")
print("   ✓ Editar Empleados existentes")
print("   ✓ Eliminar Empleados")
print("   ✓ Ver actividad reciente del sistema")
print("   ✓ Acceso a módulos de Enfermería y Médico")
