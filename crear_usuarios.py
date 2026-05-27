"""
Script oficial de creación de usuarios para el equipo de desarrollo.
Ejecutar con: python crear_usuarios.py

Crea 3 usuarios por cada perfil del sistema:
  - Administrador (superusuario)
  - Medico (staff)
  - Enfermeria
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User, Group

# ======================================================
# CREAR GRUPOS
# ======================================================
grupo_admin,      _ = Group.objects.get_or_create(name='Administrador')
grupo_medico,     _ = Group.objects.get_or_create(name='Medico')
grupo_enfermeria, _ = Group.objects.get_or_create(name='Enfermeria')

# ======================================================
# DEFINICIÓN DE USUARIOS
# ======================================================
usuarios = [
    # --- ADMINISTRADORES ---
    {
        'username': 'admin1',
        'password': 'Admin123!',
        'first_name': 'Carlos',
        'last_name': 'Ramirez',
        'email': 'admin1@gerontologia.com',
        'is_superuser': True,
        'is_staff': True,
        'group': grupo_admin,
    },
    {
        'username': 'admin2',
        'password': 'Admin123!',
        'first_name': 'Patricia',
        'last_name': 'Lopez',
        'email': 'admin2@gerontologia.com',
        'is_superuser': True,
        'is_staff': True,
        'group': grupo_admin,
    },
    {
        'username': 'admin3',
        'password': 'Admin123!',
        'first_name': 'Fernando',
        'last_name': 'Torres',
        'email': 'admin3@gerontologia.com',
        'is_superuser': True,
        'is_staff': True,
        'group': grupo_admin,
    },
    # --- MÉDICOS ---
    {
        'username': 'medico1',
        'password': 'Medico123!',
        'first_name': 'Dr. Andres',
        'last_name': 'Gutierrez',
        'email': 'medico1@gerontologia.com',
        'is_superuser': False,
        'is_staff': True,
        'group': grupo_medico,
    },
    {
        'username': 'medico2',
        'password': 'Medico123!',
        'first_name': 'Dra. Sandra',
        'last_name': 'Morales',
        'email': 'medico2@gerontologia.com',
        'is_superuser': False,
        'is_staff': True,
        'group': grupo_medico,
    },
    {
        'username': 'medico3',
        'password': 'Medico123!',
        'first_name': 'Dr. Jorge',
        'last_name': 'Herrera',
        'email': 'medico3@gerontologia.com',
        'is_superuser': False,
        'is_staff': True,
        'group': grupo_medico,
    },
    # --- ENFERMERÍA ---
    {
        'username': 'enfermera1',
        'password': 'Enfermeria123!',
        'first_name': 'Laura',
        'last_name': 'Vargas',
        'email': 'enfermera1@gerontologia.com',
        'is_superuser': False,
        'is_staff': False,
        'group': grupo_enfermeria,
    },
    {
        'username': 'enfermera2',
        'password': 'Enfermeria123!',
        'first_name': 'Diana',
        'last_name': 'Castillo',
        'email': 'enfermera2@gerontologia.com',
        'is_superuser': False,
        'is_staff': False,
        'group': grupo_enfermeria,
    },
    {
        'username': 'enfermera3',
        'password': 'Enfermeria123!',
        'first_name': 'Monica',
        'last_name': 'Rios',
        'email': 'enfermera3@gerontologia.com',
        'is_superuser': False,
        'is_staff': False,
        'group': grupo_enfermeria,
    },
]

# ======================================================
# CREAR / ACTUALIZAR USUARIOS
# ======================================================
print("=" * 60)
print("  CREACION DE USUARIOS - GERONTOLOGIA APP")
print("=" * 60)

for u in usuarios:
    user, created = User.objects.get_or_create(username=u['username'])
    user.set_password(u['password'])
    user.first_name    = u['first_name']
    user.last_name     = u['last_name']
    user.email         = u['email']
    user.is_superuser  = u['is_superuser']
    user.is_staff      = u['is_staff']
    user.is_active     = True
    user.save()
    user.groups.clear()
    user.groups.add(u['group'])
    estado = "CREADO" if created else "ACTUALIZADO"
    print(f"  [{estado}] {u['username']} ({u['group'].name})")

# ======================================================
# RESUMEN DE CREDENCIALES
# ======================================================
print("\n" + "=" * 60)
print("  CREDENCIALES DEL SISTEMA")
print("=" * 60)

print("""
ADMINISTRADORES  (acceso completo + panel admin)
  usuario: admin1    contrasena: Admin123!
  usuario: admin2    contrasena: Admin123!
  usuario: admin3    contrasena: Admin123!

MEDICOS  (modulo medico + historias)
  usuario: medico1   contrasena: Medico123!
  usuario: medico2   contrasena: Medico123!
  usuario: medico3   contrasena: Medico123!

ENFERMERIA  (modulo enfermeria)
  usuario: enfermera1  contrasena: Enfermeria123!
  usuario: enfermera2  contrasena: Enfermeria123!
  usuario: enfermera3  contrasena: Enfermeria123!

URL del sistema: http://127.0.0.1:8000
""")
print("=" * 60)
print(f"Total usuarios en sistema: {User.objects.count()}")
print("=" * 60)

