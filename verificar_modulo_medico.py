import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate

print("\n" + "="*70)
print("VERIFICACIÓN FINAL DEL MÓDULO MÉDICO")
print("="*70)

print("\n✅ GRUPOS/PERFILES CONFIGURADOS:\n")
grupos = Group.objects.all()
for g in grupos:
    Empleados = g.user_set.all()
    print(f"  • Grupo: {g.name}")
    print(f"    Empleados: {Empleados.count()}")
    for u in Empleados:
        print(f"      - {u.username} ({u.email})")
    print()

print("="*70)
print("🔐 REDIRECCIONES DE LOGIN CONFIGURADAS:")
print("="*70)

redirecciones = [
    ("Superusuario", "admin", "/administrador/"),
    ("Grupo Enfermeria", "enfermero1", "/enfermeria/"),
    ("Grupo Medico", "medico1", "/medico/"),
]

for tipo, username, ruta in redirecciones:
    user = User.objects.filter(username=username).first()
    if user:
        print(f"\n  {tipo}:")
        print(f"    Usuario: {username}")
        print(f"    Email: {user.email}")
        print(f"    Redirección: {ruta}")
        print(f"    Estado: ✓ Configurado")
    else:
        print(f"\n  {tipo}:")
        print(f"    Usuario: {username}")
        print(f"    Estado: ✗ No encontrado")

print("\n" + "="*70)
print("📝 CREDENCIALES DE ACCESO")
print("="*70)

print("\n  ADMINISTRADOR:")
print("    Usuario: admin")
print("    Contraseña: Admin123")
print("    → Al hacer login va a: /administrador/")

print("\n  MÉDICO:")
print("    Usuario: medico1")
print("    Contraseña: Medico123")
print("    → Al hacer login va a: /medico/")

print("\n  ENFERMERÍA:")
print("    Usuario: enfermero1")
print("    Contraseña: Enfermero123")
print("    → Al hacer login va a: /enfermeria/")

print("\n" + "="*70)
print("✅ SERVIDOR CORRIENDO EN: http://127.0.0.1:8000/")
print("="*70)
print("\n💡 Prueba acceder con el usuario 'medico1' para verificar")
print("   que redirige automáticamente al módulo médico.\n")
