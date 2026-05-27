import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

print("=" * 60)
print("VERIFICACIÓN DE Empleados DEL SISTEMA")
print("=" * 60)

# Verificar ADMIN
print("\n1. ADMINISTRADOR:")
print("   Usuario: admin")
admin = User.objects.filter(username='admin').first()
if admin:
    print(f"   ✓ Existe: Sí")
    print(f"   Superusuario: {admin.is_superuser}")
    print(f"   Staff: {admin.is_staff}")
    print(f"   Activo: {admin.is_active}")
    print(f"   Email: {admin.email}")
    # Verificar autenticación
    test_auth = authenticate(username='admin', password='Admin123')
    print(f"   Autenticación con 'Admin123': {'✓ CORRECTA' if test_auth else '✗ INCORRECTA'}")
else:
    print("   ✗ NO EXISTE")

# Verificar ENFERMERO
print("\n2. ENFERMERO:")
print("   Usuario: enfermero1")
enfermero = User.objects.filter(username='enfermero1').first()
if enfermero:
    print(f"   ✓ Existe: Sí")
    grupos = [g.name for g in enfermero.groups.all()]
    print(f"   Grupos: {grupos if grupos else 'Ninguno'}")
    print(f"   Staff: {enfermero.is_staff}")
    print(f"   Activo: {enfermero.is_active}")
    print(f"   Email: {enfermero.email}")
    # Verificar autenticación
    test_auth = authenticate(username='enfermero1', password='Enfermero123')
    print(f"   Autenticación con 'Enfermero123': {'✓ CORRECTA' if test_auth else '✗ INCORRECTA'}")
else:
    print("   ✗ NO EXISTE")

print("\n" + "=" * 60)
print("RESUMEN DE TODOS LOS Empleados")
print("=" * 60)
all_users = User.objects.all()
if all_users:
    for user in all_users:
        grupos = [g.name for g in user.groups.all()]
        print(f"\n• {user.username}")
        print(f"  - Superusuario: {user.is_superuser}")
        print(f"  - Grupos: {', '.join(grupos) if grupos else 'Ninguno'}")
        print(f"  - Activo: {user.is_active}")
else:
    print("\nNo hay Empleados en el sistema")

print("\n" + "=" * 60)
