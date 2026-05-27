# Guía de Configuración para Desarrollo Colaborativo
## Gerontología App

## 🎯 Objetivo

Este documento explica cómo configurar el proyecto para trabajo colaborativo en GitHub sin conflictos de base de datos.

## 🔑 Conceptos Clave

### ✅ Lo que SÍ se sube a GitHub (Repositorio Compartido)
- ✔ `settings.py` - Configuración base (sin credenciales)
- ✔ `migrations/` - Cambios en la estructura de la BD
- ✔ `.env.example` - Plantilla de variables
- ✔ `settings_local.py.example` - Plantilla de configuración
- ✔ `requirements.txt` - Dependencias del proyecto
- ✔ Código fuente (Python, HTML, CSS, JS)

### ❌ Lo que NO se sube a GitHub (Local de cada desarrollador)
- ✖ `.env` - Credenciales personales
- ✖ `settings_local.py` - Configuración personal
- ✖ `db.sqlite3` - Base de datos local
- ✖ `venv/` - Entorno virtual
- ✖ `__pycache__/` - Archivos compilados

## 🚀 Setup Inicial (Primera vez que clonas el proyecto)

```bash
# 1. Clonar el repositorio
git clone https://github.com/Manjm1012/Gerontologia-App.git
cd Gerontologia-App

# 2. Cambiar a rama develop
git checkout develop

# 3. Ejecutar script de setup automático
.\setup_dev.ps1

# 4. Editar archivo .env con TUS credenciales
# (Cada desarrollador tiene sus propias credenciales)

# 5. Crear tu base de datos local
# MySQL: CREATE DATABASE Gerontologia;

# 6. Aplicar migraciones
python manage.py migrate

# 7. Crear tu superusuario local
python manage.py createsuperuser
```

## 🔄 Workflow Diario

### Al comenzar a trabajar:

```bash
# 1. Actualizar tu rama develop
git checkout develop
git pull origin develop

# 2. Aplicar nuevas migraciones (si las hay)
python manage.py migrate

# 3. Iniciar servidor
python manage.py runserver
```

### Durante el desarrollo:

- Cada desarrollador trabaja con su propia base de datos local
- Las migraciones se comparten a través de GitHub
- Los datos NO se comparten (cada uno tiene sus propios datos de prueba)

### Al terminar:

```bash
# 1. Si creaste migraciones
python manage.py makemigrations
python manage.py migrate

# 2. Guardar cambios
git add .
git commit -m "feat: descripción del cambio"
git push origin develop
```

## 🗄️ Estrategias de Base de Datos

### Opción 1: MySQL (Recomendado para producción)
Cada desarrollador:
- Tiene su propia instalación de MySQL
- Crea su propia BD "Gerontologia"
- Configura sus credenciales en `.env`

**Ventajas:**
- Mismo motor que producción
- Detecta problemas específicos de MySQL

**Desventajas:**
- Requiere instalar y configurar MySQL

### Opción 2: SQLite (Rápido para desarrollo)
Cada desarrollador:
- Usa SQLite (viene con Python)
- No necesita instalar servidor de BD
- Configura `DB_ENGINE=sqlite3` en `.env`

**Ventajas:**
- Setup ultra rápido
- No requiere instalación adicional

**Desventajas:**
- Diferencias con MySQL de producción

## 🔧 Manejo de Migraciones

### Crear migraciones:

```bash
# Después de modificar models.py
python manage.py makemigrations

# Verificar la migración creada
python manage.py showmigrations

# Aplicar localmente
python manage.py migrate

# Subir al repositorio
git add myapp/migrations/
git commit -m "feat: añadir modelo X"
git push origin develop
```

### Aplicar migraciones de otros:

```bash
# Actualizar código
git pull origin develop

# Ver migraciones pendientes
python manage.py showmigrations

# Aplicar migraciones
python manage.py migrate
```

### Conflictos de migraciones:

Si dos desarrolladores crean migraciones simultáneamente:

```bash
# 1. Resetear migraciones locales (si no están en GitHub)
# Eliminar archivos 000X_*.py que creaste localmente

# 2. Actualizar
git pull origin develop

# 3. Recrear tus cambios
python manage.py makemigrations

# 4. Aplicar
python manage.py migrate
```

## 📊 Datos de Prueba

### Opción 1: Fixtures (Recomendado)

```bash
# Crear fixture con datos iniciales
python manage.py dumpdata myapp.ModelName > fixtures/datos_iniciales.json

# Compartir fixture en GitHub
git add fixtures/datos_iniciales.json
git commit -m "feat: añadir datos de prueba"

# Otros desarrolladores cargan los datos
python manage.py loaddata fixtures/datos_iniciales.json
```

### Opción 2: Scripts de generación

```bash
# Usar scripts existentes
python scripts/generar_Usuarios.py
python crear_Empleados.py
```

## 🔐 Seguridad

### Generar SECRET_KEY única:

```bash
# Opción 1: Online
# Visitar: https://djecrety.ir/

# Opción 2: Python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Configurar .env:

```env
SECRET_KEY=tu-secret-key-unica-aqui
DEBUG=True
DB_NAME=Gerontologia
DB_USER=root
DB_PASSWORD=tu_password_local
```

## 🐛 Solución de Problemas

### "settings.py not found"
- Ya no es un problema, settings.py ahora se sube al repo
- Asegúrate de hacer `git pull origin develop`

### "Can't connect to database"
- Verifica tus credenciales en `.env`
- Asegúrate de que MySQL esté corriendo
- Verifica que la BD exista: `CREATE DATABASE Gerontologia;`

### "Migration conflicts"
```bash
python manage.py showmigrations
python manage.py migrate --fake-initial
```

### "Module 'dotenv' not found"
```bash
pip install python-dotenv
```

## 📝 Checklist para Nuevos Desarrolladores

- [ ] Clonar repositorio
- [ ] Checkout rama develop
- [ ] Ejecutar setup_dev.ps1
- [ ] Crear archivo .env con credenciales
- [ ] Crear base de datos local
- [ ] Ejecutar migraciones
- [ ] Crear superusuario
- [ ] Probar servidor local

## 🤝 Buenas Prácticas

1. **NUNCA** commitear archivos con credenciales
2. **SIEMPRE** hacer `git pull` antes de empezar a trabajar
3. **SIEMPRE** ejecutar migraciones después de pull
4. **USAR** mensajes de commit descriptivos
5. **PROBAR** localmente antes de hacer push
6. **CREAR** ramas feature para funcionalidades grandes
7. **DOCUMENTAR** cambios importantes en el código

## 📞 Contacto

Si tienes dudas sobre la configuración, contacta a:
- Manuel Maldonado

---

**Última actualización:** Enero 2026
