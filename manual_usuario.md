**Guía Rápida para Usuario Nuevo**

- **Propósito:**: Manual paso a paso para un usuario nuevo que muestra cómo ejecutar la aplicación, navegar por las páginas y añadir capturas de pantalla de cada plantilla HTML.

**Requisitos**:
- Python 3.8+ instalado.
- Virtualenv (recomendado).
- Chrome o Edge instalado (para capturas headless opcionales).
- Dependencias del proyecto: ejecutar `pip install -r requirements.txt` en el entorno virtual.

**1. Ejecutar la aplicación (servidor de desarrollo)**
- Abrir PowerShell en la carpeta del proyecto (`c:\Users\manue\Desktop\Gerontologia\Gerontologia-App`).
- Crear y activar un entorno virtual (opcional pero recomendado):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

- Migraciones y arranque:

```powershell
python manage.py migrate
python manage.py createsuperuser   # opcional, para acceder al admin
python manage.py runserver
```

- Abrir en el navegador: `http://127.0.0.1:8000/`

**2. Carpeta de plantillas y cómo se mapean**
- Las plantillas principales están en `myapp/templates`.
- URL asociadas (según las plantillas y convenciones del proyecto):
  - `/` → `index.html`
  - `/login` → `login.html`
  - `/registro` → `registro.html`
  - `/servicios` → `servicios.html`
  - `/contactenos` → `contactenos.html`
  - `/especialidades` → `especialidades.html`
  - `/atencion` → `atencion.html`
  - `/historia_gerontologica` → `historia_gerontologica.html`
  - `/paciente` → `paciente.html`
  - `/administrador` (o ruta admin personalizada) → `administrador.html`
  - Panel/usuarios → `lista_usuarios.html` / `formulario_usuario.html` / `confirmar_borrado_usuario.html`
  - `/servicios` → `servicios.html`
  - `/somos` → `Somos.html`
  - `/terminos` → `terminos.html`
  - `/Dashboards` → `Dashboards.html`
  - `/enfermeria` → `enfermeria.html` (Módulo de Enfermería)

(Nota: las rutas exactas dependen de `urls.py` del proyecto; revise `mysite/urls.py` y `myapp/views.py` si hay dudas.)

**3. Descripción de páginas y qué mostrar en el manual (por cada plantilla)**
- **`index.html`**:
  - URL: `/`
  - Uso: página de inicio con carousel y secciones de servicios, llamada a la acción a `atencion` y `especialidades`.
  - Captura sugerida: `docs/images/index.png`.

- **`login.html`**:
  - URL: `/login`
  - Uso: formulario de inicio de sesión (usuario y contraseña).
  - Campo importante: `name="usuario"`, `name="contrasena"`.
  - Captura sugerida: `docs/images/login.png`.

- **`registro.html`**:
  - URL: `/registro`
  - Uso: crear nueva cuenta; incluye validación simple de contraseñas.
  - Captura sugerida: `docs/images/registro.png`.

- **`servicios.html`**, **`especialidades.html`** y **`atencion.html`**:
  - URL: `/servicios`, `/especialidades`, `/atencion`.
  - Uso: describen servicios, tarjetas con profesionales, botones "Solicitar Atención".
  - Capturas sugeridas: `docs/images/servicios.png`, `docs/images/especialidades.png`, `docs/images/atencion.png`.

- **`contactenos.html`**:
  - URL: `/contactenos`
  - Uso: formulario de contacto (nombre, email, teléfono, asunto, mensaje).
  - Captura sugerida: `docs/images/contactenos.png`.

- **`historia_gerontologica.html`** y **`paciente.html`**:
  - URL: `/historia_gerontologica`, `/paciente`
  - Uso: formularios extensos para la historia clínica gerontológica y ficha del paciente. Contienen muchos campos (identificación, antecedentes, revisiones por sistemas, escalas).
  - Capturas sugeridas: `docs/images/historia_gerontologica.png`, `docs/images/paciente.png`.

- **`administrador.html`, `lista_usuarios.html`, `formulario_usuario.html`, `confirmar_borrado_usuario.html`**:
  - URL: rutas de administración de usuarios (panel interno).
  - Uso: crear/editar/listar/borrar usuarios; `formulario_usuario.html` tiene campos para username, email, nombres, roles.
  - Capturas sugeridas: `docs/images/administrador.png`, `docs/images/lista_usuarios.png`, `docs/images/formulario_usuario.png`, `docs/images/confirmar_borrado.png`.

- **`Dashboards.html`**:
  - Uso: panel con indicadores y gráficos (Chart.js) para métricas de ejemplo.
  - Captura sugerida: `docs/images/dashboard.png`.

- **`terminos.html`, `Somos.html`**:
  - Uso: contenido informativo y legal.
  - Capturas sugeridas: `docs/images/terminos.png`, `docs/images/somos.png`.

- **`enfermeria.html`**:
  - URL: `/enfermeria`
  - Uso: módulo específico para usuarios con perfil de enfermería. Incluye dashboard con estadísticas del día, acciones rápidas (registro de signos vitales, control de medicamentos, notas de enfermería), tabla de pacientes del día y alertas/recordatorios.
  - Acceso: solo usuarios del grupo "Enfermeria" pueden acceder.
  - Captura sugerida: `docs/images/enfermeria.png`.

**4. Cómo generar capturas (opciones)**

Opción A — Manual (recomendado si no quieres instalar más herramientas):
- Ejecuta el servidor: `python manage.py runserver`.
- Abre cada URL en tu navegador, ajusta la ventana al tamaño deseado y presiona `PrtSc` o usa la herramienta de recorte de Windows para guardar la imagen.
- Guarda las imágenes en `docs/images/` con los nombres sugeridos.

Opción B — Usando Chrome/Edge headless (comando en PowerShell, requiere tener Chrome/Edge instalado):
- Ejecuta el servidor.
- Ejemplo con Chrome (ajusta la ruta de chrome.exe si es necesario):

```powershell
"C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu --screenshot=".\docs\images\index.png" --window-size=1280,900 http://127.0.0.1:8000/
```

- Repite cambiando la URL y el nombre de salida para cada página.
- Nota: en algunas versiones la opción `--headless=new` puede ser `--headless`.

Opción C — Usando Playwright (requiere Node.js y Playwright instalado):
- Instalar Node y luego ejecutar:

```powershell
npm init -y
npm i -D playwright
npx playwright install
```
- Script rápido (guardar como `screenshot.js`):

```javascript
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  await page.goto('http://127.0.0.1:8000/');
  await page.screenshot({ path: 'docs/images/index.png', fullPage: true });
  await browser.close();
})();
```

- Ejecutar: `node screenshot.js`.

**5. Estructura recomendada dentro del repo para el manual**
- `manual_usuario.md` (este archivo)
- `docs/images/` → colocar todas las capturas: `index.png`, `login.png`, `registro.png`, `servicios.png`, `contactenos.png`, `historia_gerontologica.png`, `paciente.png`, `administrador.png`, `lista_usuarios.png`, `dashboard.png`, `terminos.png`, `somos.png`.

**6. Ejemplo de contenido del manual para una página (plantilla `index.html`)**
- Título: Página de Inicio
- Descripción breve: Carrusel con ofertas; botones "Encuentra un profesional aquí" que abren `/atencion`.
- Elementos clave: `carousel` (img estáticas en `static/img/`), botón `href` a `{% url 'especialidades' %}`.
- Captura (incluir la imagen): `![Inicio](docs/images/index.png)`

**7. Siguientes pasos que puedo hacer por ti**


Fin del manual inicial. Si quieres, avanzo y genero las capturas automáticamente (dímelo y dime si prefieres usar Chrome headless o Playwright).
\n+**Variables opcionales (para páginas protegidas)**\n+- Crear un usuario administrativo si no existe:
**8. Automatización integrada (scripts añadidos)**
 - Script Python Playwright: `scripts/capture_screenshots.py`.
 - Script Node.js Playwright: `scripts/capture_screenshots_node.js`.
 - Crean la carpeta `docs/images` si no existe y guardan las capturas.

**Instalación (Python Playwright)**
```powershell
pip install playwright
python -m playwright install chromium
```

**Variables opcionales (para páginas protegidas)**
 - Crear usuario administrativo si no existe:
```powershell
python manage.py createsuperuser
```
 - Ajusta login si el formulario cambia (campos `usuario`, `contrasena`).

**Ejecutar el script Python (servidor ya iniciado en otra terminal)**
```powershell
python scripts/capture_screenshots.py --base-url http://127.0.0.1:8000 --out-dir docs/images --full-page
```
Con rutas admin:
```powershell
python scripts/capture_screenshots.py --base-url http://127.0.0.1:8000 --out-dir docs/images --include-admin --admin-user TU_USUARIO --admin-pass TU_CONTRASENA
```

**Ejecutar alternativa Node**
```powershell
node scripts/capture_screenshots_node.js --baseUrl http://127.0.0.1:8000 --outDir docs/images --fullPage
```

**Archivos esperados**
`index.png, login.png, registro.png, servicios.png, especialidades.png, atencion.png, contactenos.png, historia_gerontologica.png, paciente.png, administrador.png, lista_usuarios.png, formulario_usuario.png, confirmar_borrado.png, dashboard.png, terminos.png, somos.png, enfermeria.png`

**9. Mantenimiento futuro**
 - Añade nuevas rutas en `PUBLIC_ROUTES` o `ADMIN_ROUTES`.
 - Ajusta tamaño cambiando `--viewport-width/height` o el objeto `viewport`.

**10. Errores comunes**
 - "Protocol error": repetir instalación `python -m playwright install chromium`.
 - Captura vacía: incrementar `--wait-ms`.
 - Login falla: verificar nombres de campos o credenciales.

**11. Inserción de capturas en este manual**
Tras generar las imágenes, añade debajo de cada sección (o deja que se automatice) las líneas:
```markdown
![Inicio](docs/images/index.png)
![Login](docs/images/login.png)
![Registro](docs/images/registro.png)
![Servicios](docs/images/servicios.png)
![Especialidades](docs/images/especialidades.png)
![Atencion](docs/images/atencion.png)
![Contactenos](docs/images/contactenos.png)
![Historia Gerontologica](docs/images/historia_gerontologica.png)
![Paciente](docs/images/paciente.png)
![Administrador](docs/images/administrador.png)
![Lista Usuarios](docs/images/lista_usuarios.png)
![Formulario Usuario](docs/images/formulario_usuario.png)
![Confirmar Borrado](docs/images/confirmar_borrado.png)
![Dashboard](docs/images/dashboard.png)
![Terminos](docs/images/terminos.png)
![Somos](docs/images/somos.png)
![Enfermeria](docs/images/enfermeria.png)
```
Si deseas, puedo insertar automáticamente solo después de que existan para evitar referencias rotas.

**12. Extensión opcional (Selenium)**
Puedes añadir un script Selenium si tu flujo requiere interacción más compleja (llenado masivo de formularios). Solicítalo si lo necesitas.

**13. Cierre**
Manual completado. Usa los scripts para generar las capturas y luego incrusta las imágenes. Para apoyo adicional (Selenium, mejora de accesibilidad, internacionalización), indícalo.

---
Última actualización automática generada con soporte de Playwright.
\n+**14. Generar PDF del manual con las imágenes**
Requisitos: instalar librerías para PDF.
```powershell
pip install fpdf2 pillow
```
Luego generar capturas (ver sección 8) y ejecutar:
```powershell
python scripts/build_manual_pdf.py --manual manual_usuario.md --images-dir docs/images --output manual_usuario.pdf --title "Manual Usuario Gerontologia-App" --skip-missing
```
Si quieres forzar orden personalizado, crea `orden_imagenes.txt` con un nombre de archivo por línea y:
```powershell
python scripts/build_manual_pdf.py --image-order orden_imagenes.txt
```
El PDF se guardará en la raíz del proyecto como `manual_usuario.pdf`.
 
**Descarga Web del PDF**
Una vez generado, puedes descargarlo desde la aplicación:
- Enlace directo: `http://127.0.0.1:8000/manual.pdf`
- Botón/Link en la página de inicio (footer): "Descargar Manual (PDF)".
Si aparece 404, genera primero el archivo con el script.
\n+Para probar sin capturas aún (omitiéndolas):
```powershell
python scripts/build_manual_pdf.py --skip-missing
```
\n+Inserta nuevas imágenes y vuelve a ejecutar el script para regenerar el PDF.
```powershell
python manage.py createsuperuser
```
- Si tu login de administración usa `/login` con campos `usuario` y `contrasena`, puedes pasar credenciales por argumentos o editar el script directamente.\n+\n+**Ejecutar el script (servidor ya iniciado en otro terminal)**\n+```powershell
python scripts/capture_screenshots.py --base-url http://127.0.0.1:8000 --out-dir docs/images --include-admin --admin-user TU_USUARIO --admin-pass TU_CONTRASENA
```
Si no deseas páginas de administración, omite `--include-admin` y credenciales.\n+\n+**Ejecutar alternativa Node**\n+```powershell
node scripts/capture_screenshots_node.js --baseUrl http://127.0.0.1:8000 --outDir docs/images
```
\n+**Archivos generados esperados**\n+`index.png, login.png, registro.png, servicios.png, especialidades.png, atencion.png, contactenos.png, historia_gerontologica.png, paciente.png, administrador.png, lista_usuarios.png, formulario_usuario.png, confirmar_borrado.png, dashboard.png, terminos.png, somos.png`\n+\n+**9. Mantenimiento futuro**\n+- Si se agregan nuevas rutas, solo añadirlas en la lista `PUBLIC_ROUTES` o `ADMIN_ROUTES` del script.\n+- Para ajustar tamaño de ventana, modificar `viewport_width` y `viewport_height` en el script Python o el objeto `viewport` en Node.\n+\n+**10. Errores comunes**\n+- "Protocol error" al lanzar navegador: ejecutar nuevamente `python -m playwright install chromium`.\n+- Captura vacía (solo fondo): la página podría requerir datos dinámicos o demora; aumentar `--wait-ms` (Python script).\n+\n+**11. Próximo paso sugerido**\n+- Ejecutar el script para poblar `docs/images` y luego incrustar en este manual las imágenes con sintaxis Markdown.\n+- Puedo actualizar el manual insertando `![Nombre](ruta)` automáticamente tras generar las imágenes si lo solicitas.\n+\n+---\n+Actualizado para incluir automatización. Indica si deseas que agregue también un script Selenium como tercera opción.\n