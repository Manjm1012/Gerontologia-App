Markdown
# SISTEMA DE HISTORIAS GERONTOLÓGICAS
## Módulo de Enfermería – Integración de Desarrollo
**Versión:** 2.5 (Rama: `develop`)
---
## 1. Manual de Usuario – Enfermería
### 1.1 Objetivo del Módulo
Permitir el registro estructurado de la evolución diaria de las personas
mayores, incluyendo signos vitales, estado clínico y observaciones
generales en una interfaz limpia y optimizada.
### 1.2 Registro Diario de Enfermería
* **Selección de Paciente:** Al ingresar al módulo, seleccione la
persona mayor desde el listado desplegable. El sistema cargará
automáticamente la edad registrada.
* **Estado del Día y Condición Clínica:** Se registran mediante escalas
estandarizadas utilizando los parámetros **B** (Bueno), **R** (Regular) o
**M** (Malo):
* Pasó el día
* Alimentación
* Eliminación
* **Controles de Sí / No:**
* Administración de medicamentos
* Novedades clínicas
* **Signos Vitales:** Ingrese los valores numéricos correspondientes a:
* Frecuencia cardíaca (F.C.)
* Presión arterial (P.A.)
* Temperatura (T°)
* Frecuencia respiratoria (F.R.)
### 1.3 Visualización de Registro Profesional (R.P.)
El sistema permite consultar la información legal del profesional de
salud asociado al registro actual sin saturar el espacio de trabajo.
* **Acceso:** Presione el botón **“Ver R.P.”** ubicado en la celda
correspondiente.
* **Información Mostrada:** Se abrirá una ventana modal centralizada
con datos de solo lectura extraídos del perfil:
* Cédula de ciudadanía (C.C.)
* Número de matrícula profesional
* Registro único de Talento Humano en Salud (RETHUS)
* Institución de formación académica
* **Cierre:** Puede cerrar la ventana mediante el botón **“Cerrar”** o
haciendo clic fuera del recuadro modal.
### 1.4 Guardado de Registros
Al presionar el botón de guardado:
1. Se envía la información de forma segura mediante el método `POST`.
2. El sistema confirma la operación con una notificación visual en verde.
3. El formulario se limpia automáticamente, conservando por seguridad el
**profesional autenticado** y la **fecha actual**.
4. El registro se refleja en el historial inferior en tiempo real.
---
## 2. Manual Técnico (Solo Desarrollo)
### 2.1 Nota de Arquitectura
El módulo utiliza un sistema de modales dinámicos (**Bootstrap Modal**)
en lugar de tablas extensas. Esto implementa un concepto estético
minimalista y sobrio, optimizando el rendimiento de renderizado en el
frontend.
### 2.2 Fuente de Datos del R.P.
La información del profesional autenticado se mapea directamente desde la
extensión del modelo de Django:
* `user.usuario`
**Campos expuestos (Solo Lectura):** `numero_documento`,
`matricula_profesional`, `rethus`, `universidad`.
### 2.3 Consideraciones de Seguridad
* Los datos del profesional cuentan con el atributo `readonly` en el
HTML.
* Se transmiten mediante el identificador de sesión activo del backend
(`request.user`), impidiendo la suplantación de identidad o
modificaciones maliciosas desde las herramientas de desarrollador del
navegador.
---
## 3. Guía de Integración (Dev / Git Workflow)
### 3.1 Flujo Estándar de Sincronización
Para limpiar el entorno local de código roto enviado por terceros y
asegurar la última versión estable de la rama de integración, ejecute en
la terminal de VS Code:
```bash
git reset --hard HEAD
git checkout develop
git pull origin develop
