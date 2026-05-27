# Gerontología App 🏥

Aplicación desarrollada en **Django (Python)** para la gestión de información y procesos en entornos gerontológicos.

## 📋 Requisitos Previos

- Python 3.12+
- MySQL 8.0+ (o SQLite como alternativa)
- Git

## 🚀 Instalación y Configuración

### Para Nuevos Desarrolladores (Primera vez)

1. **Clonar el repositorio y cambiar a la rama develop:**
   ```bash
   git clone https://github.com/Manjm1012/Gerontologia-App.git
   cd Gerontologia-App
   git checkout develop
   ```

2. **Ejecutar el script de configuración automática:**
   ```powershell
   .\setup_dev.ps1
   ```
   
   Este script automáticamente:
   - Crea el entorno virtual
   - Instala dependencias
   - Crea archivos de configuración desde las plantillas

3. **Configurar tu entorno local:**
   
   Edita el archivo `.env` con tus credenciales:
   ```env
   DB_NAME=Gerontologia
   DB_USER=root
   DB_PASSWORD=tu_password_aqui
   DB_HOST=localhost
   DB_PORT=3306
   ```

4. **Crear la base de datos MySQL:**
   ```sql
   CREATE DATABASE Gerontologia CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

5. **Aplicar migraciones:**
   ```bash
   python manage.py migrate
   ```

6. **Crear superusuario:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Iniciar el servidor:**
   ```bash
   python manage.py runserver
   ```

### Configuración Manual (Alternativa)

Si prefieres configurar manualmente:

1. **Crear entorno virtual:**
   ```bash
   python -m venv venv
   # O si tienes múltiples versiones:
   py -3.12 -m venv venv
   ```

2. **Activar el entorno:**
   ```bash
   venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configurar archivos de entorno:**
   ```bash
   cp .env.example .env
   cp mysite\settings_local.py.example mysite\settings_local.py
   ```
   
   Luego edita `.env` con tus credenciales.

## 🔄 Workflow de Desarrollo Colaborativo

### Al iniciar tu sesión de trabajo:

```bash
# Asegurarse de estar en develop
git checkout develop

# Actualizar con los últimos cambios
git pull origin develop

# Aplicar nuevas migraciones (si las hay)
python manage.py migrate

# Iniciar servidor
python manage.py runserver
```

### Al terminar tu trabajo:

```bash
# Añadir cambios
git add .

# Commit con mensaje descriptivo
git commit -m "feat: descripción del cambio"

# Push a develop
git push origin develop
```

### Crear una nueva funcionalidad:

```bash
# Crear rama desde develop
git checkout develop
git pull origin develop
git checkout -b feature/nombre-funcionalidad

# Trabajar en tu rama...
git add .
git commit -m "feat: nueva funcionalidad"

# Subir tu rama
git push origin feature/nombre-funcionalidad

# Crear Pull Request en GitHub hacia develop
```

## 🗄️ Configuración de Base de Datos

### Opción 1: MySQL (Recomendado para producción)

```env
DB_ENGINE=mysql
DB_NAME=Gerontologia
DB_USER=root
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=3306
```

### Opción 2: SQLite (Para desarrollo local rápido)

```env
DB_ENGINE=sqlite3
```

## 📁 Estructura del Proyecto

```
Gerontologia-App/
├── mysite/              # Configuración del proyecto Django
│   ├── settings.py      # Configuración principal (SEGURO para subir a GitHub)
│   ├── settings_local.py.example  # Plantilla de configuración local
│   └── urls.py
├── myapp/               # Aplicación principal
│   ├── models.py        # Modelos de datos
│   ├── views.py         # Vistas y lógica
│   ├── templates/       # Plantillas HTML
│   ├── static/          # CSS, JS, imágenes
│   └── migrations/      # Migraciones de BD
├── .env.example         # Plantilla de variables de entorno
├── .gitignore           # Archivos ignorados por Git
├── requirements.txt     # Dependencias de Python
└── manage.py            # Script de gestión Django
```

## ⚠️ IMPORTANTE: Archivos Sensibles

**NUNCA subir a GitHub:**
- `.env` - Contiene credenciales
- `settings_local.py` - Configuración personal
- `db.sqlite3` / `db_local.sqlite3` - Base de datos local
- `__pycache__/` - Archivos compilados

**SÍ subir a GitHub:**
- `settings.py` - Ahora es seguro, usa variables de entorno
- `migrations/` - Para sincronizar estructura de BD
- `.env.example` - Plantilla sin credenciales
- `requirements.txt` - Dependencias del proyecto

## 🔧 Comandos Útiles

```bash
# Ver migraciones pendientes
python manage.py showmigrations

# Crear nuevas migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar shell de Django
python manage.py shell

# Ejecutar tests
python manage.py test

# Crear archivo de fixtures (datos de prueba)
python manage.py dumpdata myapp > fixtures/datos_prueba.json

# Cargar fixtures
python manage.py loaddata fixtures/datos_prueba.json
```

## 🐛 Solución de Problemas Comunes

### Error: "No module named 'dotenv'"
```bash
pip install python-dotenv
```

### Error: "Access denied for user 'root'@'localhost'"
- Verifica las credenciales en tu archivo `.env`
- Asegúrate de que MySQL esté corriendo

### Error: "Table doesn't exist"
```bash
python manage.py migrate
```

### Conflictos al hacer pull de develop
```bash
# Si hay conflictos en migraciones:
git pull origin develop
python manage.py migrate

# Si hay conflictos en archivos:
git stash
git pull origin develop
git stash pop
```

## 👥 Colaboradores

- Manuel Maldonado
- Danilo Lozano
- Juan Camilo Rios Mesa
- Manuela Rois Rengifo

## 📝 Convenciones de Commits

- `feat:` Nueva funcionalidad
- `fix:` Corrección de bugs
- `docs:` Cambios en documentación
- `style:` Formato, punto y coma faltantes, etc.
- `refactor:` Refactorización de código
- `test:` Añadir tests
- `chore:` Mantenimiento

## 📞 Soporte

Si encuentras problemas durante la configuración, consulta:
1. Este README.md
2. El archivo `.env.example` para ver las variables disponibles
3. El archivo `mysite/settings_local.py.example` para ver opciones de configuración

---

**Versión:** 1.0.0
**Última actualización:** Enero 2026
