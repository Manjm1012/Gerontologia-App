# 🚀 Guía para el Equipo de Desarrollo
## Configuración del Proyecto Gerontología-App

---

## 📋 ¿Qué Cambios se Hicieron?

Hemos implementado un **sistema de configuración profesional** para facilitar el trabajo colaborativo y evitar conflictos al sincronizar el proyecto desde GitHub.

### **Problema que Teníamos:**
- ❌ Conflictos con la base de datos al sincronizar
- ❌ Credenciales y contraseñas expuestas en el código
- ❌ Configuración compartida causaba problemas entre desarrolladores
- ❌ El archivo `settings.py` estaba en .gitignore (se perdía la configuración base)
- ❌ Setup manual complicado y propenso a errores

### **Solución Implementada:**
- ✅ Cada desarrollador tiene su propia base de datos local
- ✅ Credenciales protegidas con archivos `.env` (no se suben a GitHub)
- ✅ Configuración base compartida de forma segura
- ✅ Setup automático con un solo script
- ✅ Documentación completa

---

## 🎯 ¿Por Qué se Hicieron Estos Cambios?

| Cambio | Razón | Beneficio |
|--------|-------|-----------|
| **Variables de entorno (.env)** | Proteger credenciales sensibles | Cada dev tiene sus propias credenciales sin exponerlas |
| **settings_local.py** | Personalizaciones individuales | Cada dev puede tener configuraciones diferentes |
| **.gitignore actualizado** | Evitar subir archivos locales | Git ignora venv/, .env, db.sqlite3, etc. |
| **venv/ removido de Git** | El entorno virtual no debe compartirse | Cada dev crea su propio entorno |
| **setup_dev.ps1** | Automatizar configuración inicial | Setup en minutos en vez de horas |
| **python-dotenv** | Leer variables de entorno | Django carga automáticamente las credenciales |

---

## 💻 Instrucciones para Conectarse al Proyecto

### **OPCIÓN 1: Setup Automático (Recomendado) ⚡**

```powershell
# 1. Clonar el repositorio (si aún no lo tienes)
git clone https://github.com/Manjm1012/Gerontologia-App.git
cd Gerontologia-App

# 2. Cambiar a la rama develop
git checkout develop

# 3. Ejecutar el script de setup (hace todo automáticamente)
.\setup_dev.ps1
```

**El script hace todo esto por ti:**
- ✓ Crea el entorno virtual
- ✓ Instala todas las dependencias
- ✓ Crea los archivos `.env` y `settings_local.py` desde las plantillas
- ✓ Te indica los próximos pasos

### **OPCIÓN 2: Setup Manual 🔧**

```powershell
# 1. Clonar y posicionarse
git clone https://github.com/Manjm1012/Gerontologia-App.git
cd Gerontologia-App
git checkout develop

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual
.\venv\Scripts\Activate.ps1

# 4. Actualizar pip
python -m pip install --upgrade pip

# 5. Instalar dependencias
pip install -r requirements.txt

# 6. Copiar archivos de configuración
Copy-Item .env.example .env
Copy-Item mysite\settings_local.py.example mysite\settings_local.py
```

---

## ⚙️ Configuración Inicial Requerida

### **1. Configurar el archivo `.env`**

Abre el archivo `.env` (en la raíz del proyecto) y configura tus credenciales:

```env
# Configuración de Seguridad
SECRET_KEY=tu-clave-secreta-aqui-cambiar
DEBUG=True

# Configuración de Base de Datos
DB_ENGINE=mysql              # o 'sqlite' para desarrollo rápido
DB_NAME=Gerontologia        
DB_USER=root                # tu usuario de MySQL
DB_PASSWORD=tu_password     # tu contraseña de MySQL
DB_HOST=localhost
DB_PORT=3306

# Configuración Regional
LANGUAGE_CODE=es-co
TIME_ZONE=America/Bogota
```

**Opciones de Base de Datos:**

#### **Opción A: MySQL (Recomendado para producción)**
1. Instala MySQL 8.0+
2. Crea la base de datos:
   ```sql
   CREATE DATABASE Gerontologia CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
3. Configura en `.env`:
   ```env
   DB_ENGINE=mysql
   DB_NAME=Gerontologia
   DB_USER=root
   DB_PASSWORD=tu_password
   DB_HOST=localhost
   DB_PORT=3306
   ```

#### **Opción B: SQLite (Rápido para desarrollo)**
1. Configura en `.env`:
   ```env
   DB_ENGINE=sqlite
   ```
2. ¡Listo! SQLite no requiere instalación adicional

### **2. (Opcional) Personalizar `settings_local.py`**

Si necesitas configuraciones específicas para tu máquina, edita:
```
mysite/settings_local.py
```

---

## 🚀 Iniciar el Proyecto

```powershell
# 1. Activar entorno virtual (si no está activado)
.\venv\Scripts\Activate.ps1

# 2. Aplicar migraciones a la base de datos
python manage.py migrate

# 3. Crear superusuario (opcional, si necesitas acceso admin)
python manage.py createsuperuser

# 4. Iniciar servidor de desarrollo
python manage.py runserver

# 5. Abrir en el navegador
# http://127.0.0.1:8000
```

---

## 📁 Estructura de Archivos Importantes

```
Gerontologia-App/
│
├── .env                          ← TUS credenciales (NO se sube a Git)
├── .env.example                  ← Plantilla (SÍ está en Git)
├── mysite/
│   ├── settings.py               ← Configuración base (segura, en Git)
│   ├── settings_local.py         ← Tu config personal (NO en Git)
│   └── settings_local.py.example ← Plantilla (SÍ en Git)
├── requirements.txt              ← Dependencias del proyecto
├── setup_dev.ps1                 ← Script de setup automático
├── README.md                     ← Documentación principal
├── CONFIGURACION_GITHUB.md       ← Guía de colaboración Git
└── venv/                         ← Tu entorno virtual (NO en Git)
```

---

## 🔄 Flujo de Trabajo Diario

### **Al Comenzar el Día:**
```powershell
# 1. Activar entorno virtual
.\venv\Scripts\Activate.ps1

# 2. Actualizar desde GitHub
git pull origin develop

# 3. Aplicar nuevas migraciones (si hay)
python manage.py migrate

# 4. Iniciar servidor
python manage.py runserver
```

### **Al Terminar el Día:**
```powershell
# 1. Guardar cambios
git add .
git commit -m "feat: descripción de lo que hiciste"

# 2. Subir a GitHub
git push origin develop
```

---

## ⚠️ IMPORTANTE: Archivos que NUNCA debes modificar directamente

### **NO Modifiques Estos Archivos:**
- `.env.example` - Es la plantilla para todos
- `settings_local.py.example` - Es la plantilla para todos
- `.gitignore` - Configuración de Git

### **Modifica Tus Propios Archivos:**
- `.env` - Tus credenciales personales
- `settings_local.py` - Tu configuración personal

---

## 🆘 Solución de Problemas Comunes

### **Error: "No module named 'dotenv'"**
```powershell
pip install python-dotenv
```

### **Error: "Access denied for user 'root'@'localhost'"**
- Verifica tu contraseña en `.env`
- Asegúrate de que MySQL esté corriendo
- Comprueba permisos del usuario

### **Error: "No such file or directory: '.env'"**
```powershell
Copy-Item .env.example .env
# Luego edita .env con tus credenciales
```

### **El servidor no inicia**
```powershell
# 1. Verifica que el entorno virtual esté activado
.\venv\Scripts\Activate.ps1

# 2. Verifica que las dependencias estén instaladas
pip install -r requirements.txt

# 3. Verifica la configuración en .env
```

---

## 📞 Contacto y Soporte

Si tienes problemas con la configuración:

1. **Revisa primero:** README.md y CONFIGURACION_GITHUB.md
2. **Verifica:** Que tu `.env` esté correctamente configurado
3. **Confirma:** Que el entorno virtual esté activado
4. **Consulta:** Con el equipo si el problema persiste

---

## 📚 Documentos Adicionales

- **README.md** - Información general del proyecto
- **CONFIGURACION_GITHUB.md** - Workflow de Git y buenas prácticas
- **RESUMEN_CAMBIOS.md** - Detalles técnicos de los cambios

---

## ✅ Checklist de Verificación

Antes de empezar a trabajar, verifica que:

- [ ] Clonaste el repositorio desde GitHub
- [ ] Cambiaste a la rama `develop`
- [ ] Creaste y activaste el entorno virtual
- [ ] Instalaste las dependencias (`requirements.txt`)
- [ ] Creaste y configuraste tu archivo `.env`
- [ ] Aplicaste las migraciones (`python manage.py migrate`)
- [ ] El servidor inicia correctamente (`python manage.py runserver`)

**¡Listo! Ya puedes empezar a desarrollar 🎉**

---

**Última actualización:** Enero 2026  
**Versión:** 1.0  
**Rama de trabajo:** `develop`
