"""
Script de Validación del Sistema de Caché de Formularios
Verifica que el sistema de caché esté correctamente implementado
"""

import os
from pathlib import Path

# Directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent

print("=" * 80)
print("VALIDACIÓN DEL SISTEMA DE CACHÉ DE FORMULARIOS")
print("=" * 80)

# 1. Verificar que existe el archivo form_cache.js
form_cache_path = BASE_DIR / "myapp" / "static" / "js" / "form_cache.js"
print("\n1. Verificando archivo form_cache.js:")
if form_cache_path.exists():
    print(f"   ✓ Archivo encontrado: {form_cache_path}")
    file_size = form_cache_path.stat().st_size
    print(f"   ✓ Tamaño: {file_size} bytes")
    
    # Verificar contenido clave
    with open(form_cache_path, 'r', encoding='utf-8') as f:
        content = f.read()
        checks = {
            'Clase FormCache': 'class FormCache' in content,
            'localStorage': 'localStorage' in content,
            'saveToCache': 'saveToCache' in content,
            'loadFromCache': 'loadFromCache' in content,
            'clearCache': 'clearCache' in content,
            'Auto-inicialización': 'data-cache="true"' in content or 'data-cache' in content,
        }
        print("\n   Componentes detectados:")
        for component, found in checks.items():
            status = "✓" if found else "✗"
            print(f"   {status} {component}")
else:
    print(f"   ✗ Archivo NO encontrado: {form_cache_path}")

# 2. Verificar templates que usan caché
print("\n" + "=" * 80)
print("2. Formularios con caché activado:")
print("=" * 80)

templates_dir = BASE_DIR / "myapp" / "templates"
templates_with_cache = []

for template_file in templates_dir.glob("*.html"):
    with open(template_file, 'r', encoding='utf-8') as f:
        content = f.read()
        has_cache_attr = 'data-cache="true"' in content
        has_script = 'form_cache.js' in content
        
        if has_cache_attr or has_script:
            templates_with_cache.append({
                'file': template_file.name,
                'has_cache_attr': has_cache_attr,
                'has_script': has_script,
                'complete': has_cache_attr and has_script
            })

if templates_with_cache:
    for idx, template in enumerate(templates_with_cache, 1):
        status = "✓" if template['complete'] else "⚠"
        print(f"\n{status} {idx}. {template['file']}")
        print(f"   - Atributo data-cache: {'✓ Sí' if template['has_cache_attr'] else '✗ No'}")
        print(f"   - Script incluido: {'✓ Sí' if template['has_script'] else '✗ No'}")
        print(f"   - Estado: {'✓ Configurado correctamente' if template['complete'] else '⚠ Configuración incompleta'}")
else:
    print("⚠ No se encontraron templates con caché activado")

# 3. Analizar configuraciones específicas
print("\n" + "=" * 80)
print("3. Configuraciones de caché detectadas:")
print("=" * 80)

for template_file in templates_dir.glob("*.html"):
    with open(template_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
        if 'data-cache="true"' in content:
            print(f"\n📄 {template_file.name}:")
            
            # Detectar configuraciones
            import re
            
            # Buscar data-cache-interval
            interval_match = re.search(r'data-cache-interval="(\d+)"', content)
            if interval_match:
                print(f"   - Intervalo de guardado: {interval_match.group(1)} ms")
            else:
                print(f"   - Intervalo de guardado: 1000 ms (default)")
            
            # Buscar data-cache-exclude
            exclude_match = re.search(r'data-cache-exclude="([^"]+)"', content)
            if exclude_match:
                excluded_fields = exclude_match.group(1).split(',')
                print(f"   - Campos excluidos: {', '.join(excluded_fields)}")
            else:
                print(f"   - Campos excluidos: Ninguno")
            
            # Buscar data-cache-notification
            notification_match = re.search(r'data-cache-notification="(true|false)"', content)
            if notification_match:
                print(f"   - Notificaciones: {notification_match.group(1)}")
            else:
                print(f"   - Notificaciones: true (default)")

# 4. Resumen final
print("\n" + "=" * 80)
print("RESUMEN DE VALIDACIÓN")
print("=" * 80)

print(f"\n✓ Script de caché: {'Presente' if form_cache_path.exists() else 'FALTA'}")
print(f"✓ Templates con caché: {len(templates_with_cache)}")

complete_templates = sum(1 for t in templates_with_cache if t['complete'])
print(f"✓ Configuraciones completas: {complete_templates}/{len(templates_with_cache)}")

print("\n" + "=" * 80)
print("INSTRUCCIONES DE PRUEBA")
print("=" * 80)
print("""
Para verificar el funcionamiento en el navegador:

1. Inicia el servidor: python manage.py runserver
2. Abre uno de estos formularios:
   - /registro/ (Registro de usuario)
   - /historia_gerontologica/ (Historia Gerontológica)
   - /evolucion_enfermeria/ (Evolución de Enfermería)

3. Prueba el caché:
   a) Llena algunos campos del formulario
   b) Espera 1-2 segundos (verás notificación de guardado)
   c) Recarga la página (F5)
   d) Verifica que los datos se hayan restaurado

4. Para ver el caché en el navegador:
   - Abre DevTools (F12)
   - Ve a: Application > Local Storage > http://localhost:8000
   - Busca claves como: form_cache_registroForm, form_cache_historia_gerontologica_form

5. Para depuración en consola:
   FormCache.debug = true;
   // Verás logs detallados en la consola
""")

print("=" * 80)
print("✓ Validación completada")
print("=" * 80)
