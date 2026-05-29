"""
Comando de siembra inicial de datos para producción.
Ejecutar con: python manage.py seed_data

Crea de forma idempotente:
  - Grupos: Administrador, Medico, Enfermeria
  - 3 usuarios por grupo (admin, medico, enfermeria)
  - 5 pacientes de prueba (Identificacion)
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from django.db import transaction
from datetime import date


USUARIOS = [
    # Administradores
    dict(username='admin1', password='Admin123!', first_name='Carlos',
         last_name='Ramirez', email='admin1@gerontologia.com',
         is_superuser=True, is_staff=True, group='Administrador'),
    dict(username='admin2', password='Admin123!', first_name='Patricia',
         last_name='Lopez', email='admin2@gerontologia.com',
         is_superuser=True, is_staff=True, group='Administrador'),
    dict(username='admin3', password='Admin123!', first_name='Fernando',
         last_name='Torres', email='admin3@gerontologia.com',
         is_superuser=True, is_staff=True, group='Administrador'),
    # Médicos
    dict(username='medico1', password='Medico123!', first_name='Dr. Andres',
         last_name='Gutierrez', email='medico1@gerontologia.com',
         is_superuser=False, is_staff=True, group='Medico'),
    dict(username='medico2', password='Medico123!', first_name='Dra. Sandra',
         last_name='Morales', email='medico2@gerontologia.com',
         is_superuser=False, is_staff=True, group='Medico'),
    dict(username='medico3', password='Medico123!', first_name='Dr. Jorge',
         last_name='Herrera', email='medico3@gerontologia.com',
         is_superuser=False, is_staff=True, group='Medico'),
    # Enfermería
    dict(username='enfermera1', password='Enfermeria123!', first_name='Laura',
         last_name='Vargas', email='enfermera1@gerontologia.com',
         is_superuser=False, is_staff=False, group='Enfermeria'),
    dict(username='enfermera2', password='Enfermeria123!', first_name='Diana',
         last_name='Castillo', email='enfermera2@gerontologia.com',
         is_superuser=False, is_staff=False, group='Enfermeria'),
    dict(username='enfermera3', password='Enfermeria123!', first_name='Monica',
         last_name='Rios', email='enfermera3@gerontologia.com',
         is_superuser=False, is_staff=False, group='Enfermeria'),
]

PACIENTES = [
    dict(primer_nombre='María Elena', segundo_nombre='', primer_apellido='Rodríguez',
         segundo_apellido='García', numero_documento_paciente='41234567',
         tipo_documento='CC', edad=78, sexo='Femenino', fecha_nacimiento=date(1947, 3, 12),
         ciudad_residencia='Bogotá', zona_residencia='U', grupo_sanguineo='O+',
         pais_nacimiento='Colombia', departamento_nacimiento='Cundinamarca',
         ciudad_nacimiento='Bogotá'),
    dict(primer_nombre='José Alberto', segundo_nombre='', primer_apellido='Martínez',
         segundo_apellido='López', numero_documento_paciente='17345678',
         tipo_documento='CC', edad=82, sexo='Masculino', fecha_nacimiento=date(1943, 7, 5),
         ciudad_residencia='Medellín', zona_residencia='U', grupo_sanguineo='A+',
         pais_nacimiento='Colombia', departamento_nacimiento='Antioquia',
         ciudad_nacimiento='Medellín'),
    dict(primer_nombre='Carmen Rosa', segundo_nombre='', primer_apellido='Vargas',
         segundo_apellido='Herrera', numero_documento_paciente='51456789',
         tipo_documento='CC', edad=75, sexo='Femenino', fecha_nacimiento=date(1950, 11, 20),
         ciudad_residencia='Cali', zona_residencia='U', grupo_sanguineo='B+',
         pais_nacimiento='Colombia', departamento_nacimiento='Valle del Cauca',
         ciudad_nacimiento='Cali'),
    dict(primer_nombre='Luis Fernando', segundo_nombre='', primer_apellido='González',
         segundo_apellido='Pérez', numero_documento_paciente='19567890',
         tipo_documento='CC', edad=80, sexo='Masculino', fecha_nacimiento=date(1945, 1, 30),
         ciudad_residencia='Barranquilla', zona_residencia='U', grupo_sanguineo='O-',
         pais_nacimiento='Colombia', departamento_nacimiento='Atlántico',
         ciudad_nacimiento='Barranquilla'),
    dict(primer_nombre='Ana Lucía', segundo_nombre='', primer_apellido='Torres',
         segundo_apellido='Moreno', numero_documento_paciente='51678901',
         tipo_documento='CC', edad=71, sexo='Femenino', fecha_nacimiento=date(1954, 6, 8),
         ciudad_residencia='Bucaramanga', zona_residencia='U', grupo_sanguineo='AB+',
         pais_nacimiento='Colombia', departamento_nacimiento='Santander',
         ciudad_nacimiento='Bucaramanga'),
]


class Command(BaseCommand):
    help = 'Siembra grupos, usuarios y pacientes de prueba (idempotente)'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING('=' * 60))
        self.stdout.write(self.style.MIGRATE_HEADING('  SEED DATA - GERONTOLOGIA APP'))
        self.stdout.write(self.style.MIGRATE_HEADING('=' * 60))

        with transaction.atomic():
            self._seed_grupos()
            self._seed_usuarios()
            self._seed_pacientes()

        self.stdout.write(self.style.SUCCESS('\n✅ Seed completado exitosamente.\n'))
        self._print_credenciales()

    def _seed_grupos(self):
        self.stdout.write('\n--- Grupos ---')
        for nombre in ('Administrador', 'Medico', 'Enfermeria'):
            _, created = Group.objects.get_or_create(name=nombre)
            estado = 'CREADO' if created else 'ya existe'
            self.stdout.write(f'  [{estado}] {nombre}')

    def _seed_usuarios(self):
        self.stdout.write('\n--- Usuarios ---')
        for u in USUARIOS:
            grp = Group.objects.get(name=u['group'])
            user, created = User.objects.get_or_create(username=u['username'])
            user.set_password(u['password'])
            user.first_name   = u['first_name']
            user.last_name    = u['last_name']
            user.email        = u['email']
            user.is_superuser = u['is_superuser']
            user.is_staff     = u['is_staff']
            user.is_active    = True
            user.save()
            user.groups.clear()
            user.groups.add(grp)
            estado = 'CREADO' if created else 'ACTUALIZADO'
            self.stdout.write(f'  [{estado}] {u["username"]} → {u["group"]}')

    def _seed_pacientes(self):
        from myapp.models import Identificacion
        self.stdout.write('\n--- Pacientes ---')
        for p in PACIENTES:
            doc = p['numero_documento_paciente']
            _, created = Identificacion.objects.get_or_create(
                numero_documento_paciente=doc,
                defaults=p,
            )
            nombre = f'{p["primer_nombre"]} {p["primer_apellido"]}'
            estado = 'CREADO' if created else 'ya existe'
            self.stdout.write(f'  [{estado}] {nombre} ({doc})')

    def _print_credenciales(self):
        self.stdout.write(self.style.MIGRATE_HEADING('=' * 60))
        self.stdout.write(self.style.MIGRATE_HEADING('  CREDENCIALES DEL SISTEMA'))
        self.stdout.write(self.style.MIGRATE_HEADING('=' * 60))
        self.stdout.write("""
ADMINISTRADORES  (acceso completo + panel admin)
  usuario: admin1 / admin2 / admin3   contraseña: Admin123!

MÉDICOS  (módulo médico + historias)
  usuario: medico1 / medico2 / medico3   contraseña: Medico123!

ENFERMERÍA  (módulo enfermería)
  usuario: enfermera1 / enfermera2 / enfermera3   contraseña: Enfermeria123!

PACIENTES DE PRUEBA (buscar por número de documento):
  41234567  →  María Elena Rodríguez
  17345678  →  José Alberto Martínez
  51456789  →  Carmen Rosa Vargas
  19567890  →  Luis Fernando González
  51678901  →  Ana Lucía Torres
""")
        self.stdout.write(self.style.MIGRATE_HEADING('=' * 60))
