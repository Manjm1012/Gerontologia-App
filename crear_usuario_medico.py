import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User, Group

print("=" * 60)
print("CREANDO USUARIO MÉDICO")
print("=" * 60)

# Verificar si el grupo Medico existe
grupo_medico, created = Group.objects.get_or_create(name='Medico')
if created:
    print("\n✓ Grupo 'Medico' creado")
else:
    print("\n✓ Grupo 'Medico' ya existe")

# Verificar si el usuario ya existe
if User.objects.filter(username='medico1').exists():
    print("✗ El usuario 'medico1' ya existe")
    user = User.objects.get(username='medico1')
    print("  Actualizando configuración...")
else:
    # Crear el usuario
    user = User.objects.create_user(
        username='medico1',
        email='medico1@gerontologia.com',
        password='Medico123',
        first_name='Médico',
        last_name='Uno'
    )
    user.is_staff = True  # Puede acceder al admin si es necesario
    user.save()
    print("✓ Usuario 'medico1' creado exitosamente")

# Agregar al grupo de Medico
if grupo_medico not in user.groups.all():
    user.groups.add(grupo_medico)
    print("✓ Usuario agregado al grupo 'Medico'")
else:
    print("✓ Usuario ya pertenece al grupo 'Medico'")

print("\n" + "=" * 60)
print("INFORMACIÓN DEL USUARIO CREADO")
print("=" * 60)
print(f"\nUsuario: {user.username}")
print(f"Email: {user.email}")
print(f"Nombre completo: {user.get_full_name()}")
print(f"Contraseña: Medico123")
print(f"Es staff: {user.is_staff}")
print(f"Es superusuario: {user.is_superuser}")
print(f"Grupos: {', '.join([g.name for g in user.groups.all()])}")
print(f"Activo: {user.is_active}")

print("\n" + "=" * 60)
print("RESUMEN")
print("=" * 60)
print("\n✓ Grupo 'Medico' disponible")
print("✓ Usuario 'medico1' configurado")
print("\n📝 Credenciales de acceso:")
print("   Usuario: medico1")
print("   Contraseña: Medico123")
print("=" * 60)
