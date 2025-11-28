# Formulario de Evolución Diaria de Enfermería

## Descripción

Formulario digital para el registro diario de evolución de personas mayores en el módulo de enfermería. Replica el formato del documento físico "EVOLUCIÓN DIARIA DE ENFERMERÍA PERSONAS MAYORES".

## Campos del Formulario

### Información del Paciente
- **Nombre**: Selector de pacientes registrados en el sistema
- **Edad**: Se autocompleta al seleccionar el paciente
- **Diagnóstico**: Campo libre para diagnóstico

### Registro Diario
Cada fila de la tabla contiene:

1. **Fecha** (D-M-A): Fecha del registro
2. **Pasó el Día** (B-R-M): 
   - B = Bueno
   - R = Regular
   - M = Malo
3. **Alimentación** (B-R-M): Estado de la alimentación
4. **Elimina** (B-R-M): Micción/orina
5. **Exonera** (B-R-M): Deposición
6. **Medicamentos** (SI-NO): Si recibió medicación
7. **Signos Vitales**:
   - **F.C.**: Frecuencia Cardíaca
   - **P.A.**: Presión Arterial
   - **T**: Temperatura
   - **F.R.**: Frecuencia Respiratoria
8. **Novedad** (SI-NO): Si hubo alguna novedad
9. **Observación**: Campo de texto libre
10. **Nombre de quien atiende**: Nombre del profesional de enfermería
11. **Identificación**: Documento del profesional
12. **Firma**: Firma digital o nombre

## Acceso al Formulario

### Desde el Dashboard de Enfermería
1. Iniciar sesión con usuario de enfermería
2. En el dashboard, hacer clic en "Evolución Diaria"
3. Se abrirá el formulario de registro

### URL Directa
`http://127.0.0.1:8000/enfermeria/evolucion/`

## Uso del Formulario

### Registrar una Evolución

1. **Seleccionar Paciente**:
   - Elegir del desplegable "Nombre"
   - La edad se llenará automáticamente
   - Agregar diagnóstico si es necesario

2. **Completar Registro Diario**:
   - Fecha (por defecto es hoy)
   - Seleccionar estado del día (B/R/M)
   - Seleccionar estado de alimentación
   - Seleccionar estado de eliminación
   - Seleccionar estado de exoneración
   - Indicar si recibió medicamentos
   - Ingresar signos vitales (opcional pero recomendado)
   - Indicar si hay novedades
   - Agregar observaciones importantes

3. **Datos del Profesional**:
   - El nombre se autocompleta con el usuario actual
   - Ingresar número de identificación
   - Agregar firma (opcional)

4. **Guardar**:
   - Hacer clic en "Guardar Registro"
   - Aparecerá un mensaje de confirmación

### Agregar Múltiples Registros
- Usar el botón "Agregar Fila" para registrar múltiples evoluciones en la misma sesión
- Cada fila es independiente pero todas se guardarán al presionar "Guardar Registro"

## Historial de Evoluciones

En la parte inferior del formulario se muestra una tabla con las últimas 20 evoluciones registradas:

- Fecha del registro
- Nombre del paciente
- Estado del día
- Signos vitales principales
- Si hubo novedades
- Profesional que registró

## Modelo de Base de Datos

```python
class EvolucionDiariaEnfermeria(models.Model):
    paciente = ForeignKey('Identificacion')
    fecha = DateField()
    paso_el_dia = CharField(choices=['B','R','M'])
    alimentacion = CharField(choices=['B','R','M'])
    elimina = CharField(choices=['B','R','M'])
    exonera = CharField(choices=['B','R','M'])
    medicamentos = CharField(choices=['SI','NO'])
    frecuencia_cardiaca = CharField(max_length=10)
    presion_arterial = CharField(max_length=10)
    temperatura = CharField(max_length=10)
    frecuencia_respiratoria = CharField(max_length=10)
    novedad = CharField(choices=['SI','NO'])
    observacion = TextField()
    nombre_profesional = CharField(max_length=255)
    identificacion_profesional = CharField(max_length=50)
    firma = CharField(max_length=255)
    fecha_registro = DateTimeField(auto_now_add=True)
    usuario_registro = ForeignKey(User)
```

## Instalación y Configuración

### 1. Ejecutar Migraciones

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 2. Verificar Permisos
El usuario debe pertenecer al grupo "Enfermeria". Si no está asignado:

```powershell
python manage.py shell
```

```python
from django.contrib.auth.models import User, Group
user = User.objects.get(username='nombre_usuario')
grupo = Group.objects.get(name='Enfermeria')
user.groups.add(grupo)
user.save()
```

### 3. Crear Pacientes de Prueba
Si no hay pacientes en el sistema, crear algunos usando el formulario de historia gerontológica o desde el shell:

```python
from myapp.models import Identificacion

paciente = Identificacion.objects.create(
    primer_nombre='Juan',
    primer_apellido='Pérez',
    edad=75,
    tipo_documento='CC',
    numero_documento_paciente='123456789',
    # ... otros campos requeridos
)
```

## Características Técnicas

### Frontend
- HTML5 con Django Templates
- CSS sincronizado con `historia_gerontologica.css`
- JavaScript vanilla para interactividad
- Responsive design

### Backend
- Django 5.2.7
- Modelo ORM para persistencia
- Validación de formularios
- Mensajes de éxito/error
- Protección CSRF

### Seguridad
- `@login_required` decorator
- Verificación de grupo "Enfermeria"
- Validación de datos en backend
- Protección contra SQL injection (ORM)

## Reportes y Consultas

### Consultar Evoluciones de un Paciente
```python
from myapp.models import EvolucionDiariaEnfermeria, Identificacion

paciente = Identificacion.objects.get(numero_documento_paciente='123456789')
evoluciones = EvolucionDiariaEnfermeria.objects.filter(paciente=paciente).order_by('-fecha')
```

### Evoluciones de un Rango de Fechas
```python
from datetime import date
evoluciones = EvolucionDiariaEnfermeria.objects.filter(
    fecha__range=[date(2025, 1, 1), date(2025, 12, 31)]
)
```

### Pacientes con Novedades
```python
evoluciones_con_novedad = EvolucionDiariaEnfermeria.objects.filter(novedad='1')
```

## Futuras Mejoras

- [ ] Exportar evoluciones a PDF
- [ ] Gráficos de signos vitales históricos
- [ ] Alertas automáticas por valores anormales
- [ ] Firma digital con tablet/stylus
- [ ] Búsqueda avanzada de registros
- [ ] Estadísticas por profesional
- [ ] Integración con historia gerontológica
- [ ] Notificaciones de novedades
- [ ] Impresión de reportes mensuales

## Soporte

Para problemas o consultas sobre el formulario de evolución diaria, contactar al equipo de desarrollo o revisar la documentación del módulo de enfermería en `MODULO_ENFERMERIA.md`.

---

**Última actualización**: Noviembre 2025  
**Versión**: 1.0.0
