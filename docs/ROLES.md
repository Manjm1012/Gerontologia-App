# Mapeo de Roles (Grupos) → Módulos

Este documento describe los grupos (roles) del sistema y los módulos a los que dan acceso, además de comandos útiles para crear y verificar los roles/usuarios en entornos de desarrollo/producción.

## Grupos y módulos

- **Medico** : acceso al módulo `medico` ([myapp/views.py](myapp/views.py#L1000-L1020)).
- **Enfermeria** : acceso al módulo `enfermeria` ([myapp/views.py](myapp/views.py#L808)).
- **Psicologo** : acceso al módulo `psicologo` (plantilla `psicologo.html`).
- **Fisioterapia** : acceso al módulo `fisioterapia` (plantilla `fisioterapia.html`).
- **Fonoaudiologia** : acceso al módulo `fonoaudiologia` (plantilla `fonoaudiologia.html`).
- **Administrativo** : acceso a pantallas administrativas limitadas (crear usuarios, listados).
- **Staff / Superuser** : acceso completo a `admin` y a funcionalidades administrativas.

> Nota: las comprobaciones de pertenencia a grupos se realizan mediante `request.user.groups.filter(name='...').exists()`.

## Comandos útiles

1) Crear roles (si existe el comando `create_roles` en `myapp.management.commands`):

```powershell
.\'venv\Scripts\python.exe' manage.py create_roles --names "Medico,Enfermeria,Psicologo,Fisioterapia,Fonoaudiologia,Administrativo"
```

2) Ver roles y usuarios (si existe el comando `verify_profiles`):

```powershell
.\'venv\Scripts\python.exe' manage.py verify_profiles
```

3) Crear usuarios de prueba por perfil (usa el comando `create_test_users` que se agregó durante la QA):

```powershell
.\'venv\Scripts\python.exe' manage.py create_test_users
# Contraseña por defecto: ChangeMe123!
```

4) Alternativa manual (Django shell) para crear un rol y asignarlo a un usuario:

```python
from django.contrib.auth.models import Group, User
grp, _ = Group.objects.get_or_create(name='Medico')
u = User.objects.create_user('medico_test', password='ChangeMe123!')
u.groups.add(grp)
u.save()
```

## Recomendaciones para producción

- Ejecutar la creación de roles una sola vez en despliegue (o incluir en scripts de migración/seed).
- Mantener contraseñas seguras al crear cuentas reales — los usuarios de prueba deben ser rotados o eliminados.
- Revisar `settings.py` y fijar `LOGIN_URL = 'login'` para uniformidad en redirecciones.
- Documentar cualquier cambio adicional en la asignación de grupos si aparecen nuevos módulos.

## Contacto

Para dudas sobre permisos o mapeos, revisa `myapp/views.py` y las plantillas dentro de `myapp/templates/`.
