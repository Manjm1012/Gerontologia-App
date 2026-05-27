# Módulo de Enfermería - Gerontología App

## Descripción

El módulo de enfermería es una interfaz especializada diseñada para el personal de enfermería que trabaja con Usuarios gerontológicos. Proporciona acceso rápido a funcionalidades críticas del día a día.

## Características Principales

### 📊 Dashboard de Estadísticas
- Usuarios atendidos del día
- Consultas pendientes
- Signos vitales tomados
- Medicamentos administrados

### ⚡ Acciones Rápidas
1. **Registro de Signos Vitales**: Tomar y registrar presión arterial, temperatura, pulso, etc.
2. **Control de Medicamentos**: Administrar y documentar medicación
3. **Notas de Enfermería**: Registrar observaciones y evolución del paciente
4. **Historial de Usuarios**: Consultar historia clínica completa
5. **Citas Programadas**: Ver agenda del día
6. **Procedimientos**: Registro de curaciones y otros procedimientos

### 👥 Gestión de Usuarios
- Vista de tabla con Usuarios del día
- Información rápida: documento, nombre, edad, última atención, estado
- Botones de acción rápida por paciente

### 🔔 Alertas y Recordatorios
- Medicamentos pendientes por administrar
- Recordatorios de controles periódicos
- Notificaciones importantes

## Instalación y Configuración

### 1. Ejecutar Migraciones

```powershell
python manage.py migrate
```

Esto creará automáticamente el grupo "Enfermeria" en el sistema.

### 2. Crear Usuario de Enfermería

Tienes dos opciones:

#### Opción A: Desde el Panel de Administración
1. Inicia sesión como administrador
2. Ve a `http://127.0.0.1:8000/admin/users/`
3. Crea un nuevo usuario
4. Asigna el perfil "Enfermeria"

#### Opción B: Desde la Consola de Django

```powershell
python manage.py shell
```

```python
from django.contrib.auth.models import User, Group

# Crear usuario
usuario = User.objects.create_user(
    username='enfermera1',
    email='enfermera1@ejemplo.com',
    password='contraseña123',
    first_name='María',
    last_name='García'
)

# Asignar al grupo Enfermeria
grupo_enfermeria = Group.objects.get(name='Enfermeria')
usuario.groups.add(grupo_enfermeria)
usuario.save()

print(f"Usuario {usuario.username} creado y asignado al grupo Enfermeria")
```

### 3. Acceder al Módulo

1. Ir a `http://127.0.0.1:8000/login`
2. Iniciar sesión con las credenciales del usuario de enfermería
3. Serás redirigido automáticamente a `/enfermeria`

## Estructura de Archivos

```
myapp/
├── templates/
│   └── enfermeria.html          # Template principal del módulo
├── static/
│   ├── CSS/
│   │   └── enfermeria.css       # Estilos específicos
│   └── js/
│       └── enfermeria.js        # Scripts JavaScript
├── views.py                     # Vista enfermeria()
└── migrations/
    └── 0007_crear_grupo_enfermeria.py  # Migración del grupo
```

## Seguridad y Permisos

El módulo de enfermería está protegido con:

1. **@login_required**: Solo Empleados autenticados pueden acceder
2. **Verificación de Grupo**: Solo miembros del grupo "Enfermeria" pueden acceder
3. **Redirección Automática**: Empleados no autorizados son redirigidos con mensaje de error

## Personalización

### Agregar Nuevas Estadísticas

Edita `views.py` en la función `enfermeria()`:

```python
context = {
    'Usuarios': Usuarios,
    'Usuarios_atendidos': Identificacion.objects.filter(...).count(),
    'consultas_pendientes': 5,
    'signos_vitales': 12,
    'medicamentos_admin': 8,
    # Agrega más estadísticas aquí
}
```

### Agregar Nuevas Acciones

Edita `enfermeria.html` en la sección `actions-grid`:

```html
<a href="#nueva-accion" class="action-card">
    <div class="action-icon">
        <i class="fas fa-nuevo-icono"></i>
    </div>
    <h3>Nueva Acción</h3>
    <p>Descripción de la nueva funcionalidad</p>
</a>
```

### Modificar Estilos

Edita `myapp/static/CSS/enfermeria.css` para personalizar:
- Colores del tema
- Tamaños de fuente
- Animaciones
- Diseño responsive

## Integración con Base de Datos

El módulo actualmente muestra datos del modelo `Identificacion`. Para integrarlo completamente:

1. Crea modelos para:
   - SignosVitales
   - NotasEnfermeria
   - ControlMedicamentos
   - Procedimientos

2. Actualiza la vista para consultar estos modelos

3. Crea formularios para captura de datos

## Funcionalidades Futuras Planificadas

- [ ] Formulario de registro de signos vitales
- [ ] Sistema de alertas en tiempo real
- [ ] Generación de reportes diarios
- [ ] Integración con historia gerontológica
- [ ] Notificaciones push
- [ ] Calendario de turnos
- [ ] Chat interno con otros profesionales

## Problemas Comunes

### Error: "No tiene permisos para acceder a este módulo"

**Solución**: Verifica que el usuario esté en el grupo "Enfermeria"

```python
# En Django shell
from django.contrib.auth.models import User, Group
user = User.objects.get(username='tu_usuario')
grupo = Group.objects.get(name='Enfermeria')
user.groups.add(grupo)
user.save()
```

### Error 404 en /enfermeria

**Solución**: Verifica que la URL esté registrada en `urls.py`:

```python
path('enfermeria/', views.enfermeria, name='enfermeria'),
```

### Los estilos no se cargan

**Solución**: Ejecuta collectstatic si estás en producción:

```powershell
python manage.py collectstatic
```

## Soporte

Para reportar problemas o solicitar nuevas funcionalidades, contacta al equipo de desarrollo.

---

**Última actualización**: Noviembre 2025
**Versión**: 1.0.0
