import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User, Group

print("=" * 60)
print("DIAGNÓSTICO DE LOGIN - Usuario enfermero1")
print("=" * 60)

# Verificar usuario
user = User.objects.get(username='enfermero1')
print(f"\nUsuario: {user.username}")
print(f"Activo: {user.is_active}")
print(f"Staff: {user.is_staff}")
print(f"Superusuario: {user.is_superuser}")

# Verificar grupos
grupos_usuario = [g.name for g in user.groups.all()]
print(f"\nGrupos del usuario: {grupos_usuario}")

# Mostrar todos los grupos
all_groups = Group.objects.all()
print(f"\nTodos los grupos en el sistema:")
for g in all_groups:
    print(f"  - '{g.name}'")

# Verificar coincidencias
print("\nVerificación de coincidencias:")
print(f"  - Coincide con 'Enfermeria' (sin tilde): {user.groups.filter(name='Enfermeria').exists()}")
print(f"  - Coincide con 'Enfermería' (con tilde): {user.groups.filter(name='Enfermería').exists()}")

# Simular la lógica del login
print("\n" + "=" * 60)
print("SIMULACIÓN DE LÓGICA DE REDIRECCIÓN")
print("=" * 60)

if user.is_active:
    if user.is_superuser:
        print("✓ Debería redirigir a: /administrador/ (superusuario)")
    elif user.groups.filter(name='Enfermeria').exists():
        print("✓ Debería redirigir a: /enfermeria/ (grupo Enfermeria)")
    elif user.groups.filter(name='Enfermería').exists():
        print("⚠ Coincide con 'Enfermería' pero el código busca 'Enfermeria'")
        print("  PROBLEMA: Nombre del grupo no coincide con el código")
    elif user.groups.filter(name='Medico').exists():
        print("✓ Debería redirigir a: /medico/ (grupo Medico)")
    elif user.is_staff:
        print("✓ Debería redirigir a: /administrador/ (staff)")
    else:
        print("✓ Debería redirigir a: /paciente_registro/ (default)")
else:
    print("✗ Usuario inactivo")

print("\n" + "=" * 60)
