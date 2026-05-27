import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User, Group

print("=" * 60)
print("CREANDO USUARIO DE ENFERMERÍA")
print("=" * 60)

# Verificar si el grupo Enfermería existe
grupo_enfermeria, created = Group.objects.get_or_create(name='Enfermería')
if created:
    print("\n✓ Grupo 'Enfermería' creado")
else:
    print("\n✓ Grupo 'Enfermería' ya existe")

# Verificar si el usuario ya existe
if User.objects.filter(username='enfermero1').exists():
    print("✗ El usuario 'enfermero1' ya existe")
    user = User.objects.get(username='enfermero1')
else:
    # Crear el usuario
    user = User.objects.create_user(
        username='enfermero1',
        email='enfermero1@gerontologia.com',
        password='Enfermero123',
        first_name='Enfermero',
        last_name='Uno'
    )
    user.is_staff = True  # Puede acceder al admin si es necesario
    user.save()
    print("✓ Usuario 'enfermero1' creado exitosamente")

# Agregar al grupo de Enfermería
user.groups.add(grupo_enfermeria)
print("✓ Usuario agregado al grupo 'Enfermería'")

print("\n" + "=" * 60)
print("INFORMACIÓN DEL USUARIO CREADO")
print("=" * 60)
print(f"\nUsuario: {user.username}")
print(f"Email: {user.email}")
print(f"Nombre completo: {user.get_full_name()}")
print(f"Es staff: {user.is_staff}")
print(f"Es superusuario: {user.is_superuser}")
print(f"Grupos: {', '.join([g.name for g in user.groups.all()])}")
print(f"Activo: {user.is_active}")

print("\n" + "=" * 60)
print("CREDENCIALES DE ACCESO")
print("=" * 60)
print(f"\nUsuario: enfermero1")
print(f"Contraseña: Enfermero123")
print("\n" + "=" * 60)

# Verificar autenticación
from django.contrib.auth import authenticate
test_auth = authenticate(username='enfermero1', password='Enfermero123')
if test_auth:
    print("✓ Autenticación verificada - El usuario puede iniciar sesión")
else:
    print("✗ Error en la autenticación")

print("=" * 60)
