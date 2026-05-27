# ============================================
# SCRIPT DE CONFIGURACIÓN INICIAL
# Gerontología App - Setup para Desarrolladores
# ============================================

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  SETUP GERONTOLOGÍA APP - DEVELOP" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Verificar Python
Write-Host "[1/7] Verificando instalación de Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ $pythonVersion encontrado" -ForegroundColor Green
} catch {
    Write-Host "✗ Python no encontrado. Por favor instala Python 3.12+" -ForegroundColor Red
    exit 1
}

# Crear entorno virtual
Write-Host "`n[2/7] Creando entorno virtual..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "✓ Entorno virtual ya existe" -ForegroundColor Green
} else {
    python -m venv venv
    Write-Host "✓ Entorno virtual creado" -ForegroundColor Green
}

# Activar entorno virtual
Write-Host "`n[3/7] Activando entorno virtual..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1
Write-Host "✓ Entorno virtual activado" -ForegroundColor Green

# Actualizar pip
Write-Host "`n[4/7] Actualizando pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip --quiet
Write-Host "✓ pip actualizado" -ForegroundColor Green

# Instalar dependencias
Write-Host "`n[5/7] Instalando dependencias..." -ForegroundColor Yellow
if (Test-Path "requirements.txt") {
    pip install -r requirements.txt --quiet
    Write-Host "✓ Dependencias instaladas" -ForegroundColor Green
} else {
    Write-Host "✗ No se encontró requirements.txt" -ForegroundColor Red
}

# Configurar archivo .env
Write-Host "`n[6/7] Configurando archivo de entorno..." -ForegroundColor Yellow
if (-not (Test-Path ".env")) {
    if (Test-Path ".env.example") {
        Copy-Item ".env.example" ".env"
        Write-Host "✓ Archivo .env creado desde .env.example" -ForegroundColor Green
        Write-Host "  ⚠ IMPORTANTE: Edita el archivo .env con tus credenciales locales" -ForegroundColor Yellow
    } else {
        Write-Host "✗ No se encontró .env.example" -ForegroundColor Red
    }
} else {
    Write-Host "✓ Archivo .env ya existe" -ForegroundColor Green
}

# Configurar settings_local.py
Write-Host "`n[7/7] Configurando settings_local.py..." -ForegroundColor Yellow
if (-not (Test-Path "mysite\settings_local.py")) {
    if (Test-Path "mysite\settings_local.py.example") {
        Copy-Item "mysite\settings_local.py.example" "mysite\settings_local.py"
        Write-Host "✓ settings_local.py creado desde plantilla" -ForegroundColor Green
        Write-Host "  ⚠ IMPORTANTE: Edita mysite\settings_local.py con tu configuración" -ForegroundColor Yellow
    }
} else {
    Write-Host "✓ settings_local.py ya existe" -ForegroundColor Green
}

# Resumen final
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  CONFIGURACIÓN COMPLETADA" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "PRÓXIMOS PASOS:" -ForegroundColor White
Write-Host "1. Edita el archivo .env con tus credenciales de base de datos" -ForegroundColor White
Write-Host "2. Ejecuta las migraciones: python manage.py migrate" -ForegroundColor White
Write-Host "3. Crea un superusuario: python manage.py createsuperuser" -ForegroundColor White
Write-Host "4. Inicia el servidor: python manage.py runserver`n" -ForegroundColor White

Write-Host "CONFIGURACIÓN DE BASE DE DATOS:" -ForegroundColor Yellow
Write-Host "- MySQL: Asegúrate de tener MySQL instalado y la BD 'Gerontologia' creada" -ForegroundColor White
Write-Host "- SQLite: Cambia DB_ENGINE=sqlite3 en el archivo .env para usar SQLite`n" -ForegroundColor White

Write-Host "Para más información, consulta README.md" -ForegroundColor Cyan
