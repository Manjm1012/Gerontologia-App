import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Verificar si existe el usuario admin
try:
    admin = User.objects.get(username='admin')
    print(f"✓ Usuario encontrado: {admin.username}")
    print(f"  - Email: {admin.email}")
    print(f"  - is_superuser: {admin.is_superuser}")
    print(f"  - is_staff: {admin.is_staff}")
    print(f"  - is_active: {admin.is_active}")
    print(f"  - Fecha creación: {admin.date_joined}")
    
    # Probar autenticación con diferentes contraseñas
    print("\n--- Probando autenticación ---")
    
    passwords_to_test = ['Admin123', 'admin123', 'Admin123!', 'admin']
    
    for pwd in passwords_to_test:
        user = authenticate(username='admin', password=pwd)
        if user:
            print(f"✓ Contraseña CORRECTA: '{pwd}'")
            break
        else:
            print(f"✗ Contraseña incorrecta: '{pwd}'")
    
    if not user:
        print("\n⚠ Ninguna contraseña funcionó. Reseteando contraseña...")
        admin.set_password('Admin123')
        admin.save()
        print("✓ Contraseña reseteada a: Admin123")
        
        # Verificar que ahora funcione
        user = authenticate(username='admin', password='Admin123')
        if user:
            print("✓ Autenticación exitosa con nueva contraseña")
        else:
            print("✗ Aún hay problemas con la autenticación")
            
except User.DoesNotExist:
    print("✗ El usuario 'admin' no existe")
    print("\nCreando nuevo superusuario...")
    admin = User.objects.create_superuser(
        username='admin',
        email='admin@gerontologia.com',
        password='Admin123',
        first_name='Administrador',
        last_name='Sistema'
    )
    print(f"✓ Superusuario creado: {admin.username}")
    print(f"  - Contraseña: Admin123")
    print(f"  - is_superuser: {admin.is_superuser}")
    print(f"  - is_staff: {admin.is_staff}")
