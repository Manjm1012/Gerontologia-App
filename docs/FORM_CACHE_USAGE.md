# 📝 Sistema de Cache para Formularios - Guía de Uso

## 🎯 Propósito

El sistema de cache automático guarda los datos del formulario en el navegador del usuario mientras lo está llenando, evitando pérdida de información si:
- El usuario recarga accidentalmente la página
- El navegador se cierra inesperadamente
- Hay problemas de conexión temporales
- El usuario necesita pausar y volver más tarde

## ⚡ Instalación Rápida

### Paso 1: Incluir el script

Agrega al final de tu template (antes de `</body>`):

```html
<script src="{% static 'js/form_cache.js' %}"></script>
```

### Paso 2: Activar en el formulario

Agrega el atributo `data-cache="true"` a tu formulario:

```html
<form id="mi_formulario" method="post" data-cache="true">
    <!-- tus campos -->
</form>
```

¡Eso es todo! El cache ya está funcionando.

## 🔧 Configuración Avanzada

### Opciones via atributos HTML

```html
<form id="mi_formulario" 
      method="post"
      data-cache="true"
      data-cache-interval="2000"
      data-cache-notification="true"
      data-cache-clear-on-submit="true"
      data-cache-exclude="password,cvv,tarjeta">
    <!-- campos -->
</form>
```

| Atributo | Descripción | Valores | Default |
|----------|-------------|---------|---------|
| `data-cache` | Activa el cache | `true`/`false` | `false` |
| `data-cache-interval` | Tiempo entre guardados (ms) | Número | `1000` |
| `data-cache-notification` | Mostrar notificaciones | `true`/`false` | `true` |
| `data-cache-clear-on-submit` | Limpiar al enviar | `true`/`false` | `true` |
| `data-cache-exclude` | Campos a excluir (separados por comas) | String | `""` |
| `data-cache-debug` | Modo depuración | `true`/`false` | `false` |

### Inicialización programática

Si necesitas más control:

```javascript
// Inicializar con opciones personalizadas
const cache = new FormCache('mi_formulario', {
    saveInterval: 2000,              // Guardar cada 2 segundos
    showNotification: true,          // Mostrar notificación de guardado
    clearOnSubmit: true,             // Limpiar cache al enviar
    excludeFields: ['password', 'cvv'], // Excluir estos campos
    debug: false                     // Modo depuración
});

// Métodos disponibles
cache.saveToCache();        // Forzar guardado manual
cache.clearCache();         // Limpiar cache
cache.hasCache();           // Verificar si hay cache
cache.getCacheInfo();       // Obtener info del cache
```

## 📋 Ejemplos por Tipo de Formulario

### Formulario Simple (Contacto)

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Contacto</title>
</head>
<body>
    <form id="contacto_form" method="post" data-cache="true">
        {% csrf_token %}
        <input type="text" name="nombre" placeholder="Nombre">
        <input type="email" name="email" placeholder="Email">
        <textarea name="mensaje" placeholder="Mensaje"></textarea>
        <button type="submit">Enviar</button>
    </form>
    
    <script src="{% static 'js/form_cache.js' %}"></script>
</body>
</html>
```

### Formulario de Registro (Excluir contraseñas)

```html
<form id="registro_form" 
      method="post" 
      data-cache="true"
      data-cache-exclude="password,confirm_password">
    {% csrf_token %}
    <input type="text" name="username">
    <input type="email" name="email">
    <input type="password" name="password">         <!-- No se guarda -->
    <input type="password" name="confirm_password"> <!-- No se guarda -->
    <button type="submit">Registrarse</button>
</form>

<script src="{% static 'js/form_cache.js' %}"></script>
```

### Formulario Largo (Historia Clínica)

```html
<form id="historia_clinica_form" 
      method="post" 
      data-cache="true"
      data-cache-interval="3000"
      data-cache-notification="true">
    {% csrf_token %}
    
    <!-- Identificación -->
    <input type="text" name="primer_nombre">
    <input type="text" name="primer_apellido">
    <input type="date" name="fecha_nacimiento">
    
    <!-- Antecedentes (muchos campos...) -->
    <textarea name="antecedentes_medicos"></textarea>
    <textarea name="antecedentes_familiares"></textarea>
    
    <!-- ...más campos... -->
    
    <button type="submit">Guardar Historia</button>
</form>

<script src="{% static 'js/form_cache.js' %}"></script>
```

### Formulario con Lógica Personalizada

```html
<form id="custom_form" method="post">
    {% csrf_token %}
    <!-- campos -->
</form>

<script src="{% static 'js/form_cache.js' %}"></script>
<script>
    // Inicializar con control total
    const miCache = new FormCache('custom_form', {
        saveInterval: 5000,
        showNotification: false,
        clearOnSubmit: false,  // Mantener cache después de enviar
        excludeFields: ['campo_temporal'],
        debug: true
    });
    
    // Lógica personalizada
    document.querySelector('button[type="submit"]').addEventListener('click', (e) => {
        // Guardar antes de enviar
        miCache.saveToCache();
        
        // Confirmar si quiere limpiar el cache
        if (confirm('¿Limpiar datos guardados?')) {
            miCache.clearCache();
        }
    });
    
    // Mostrar info del cache
    const info = miCache.getCacheInfo();
    if (info) {
        console.log(`Datos guardados hace ${info.timestamp}`);
        console.log(`Total de campos: ${info.fieldsCount}`);
    }
</script>
```

## 🎨 Personalizar Notificaciones

Las notificaciones usan estilos inline. Para personalizar, puedes modificar `form_cache.js` o sobrescribir con CSS:

```css
/* Personalizar notificación de guardado */
#form-cache-indicator {
    background: #10b981 !important;  /* Verde */
    bottom: 30px !important;
    right: 30px !important;
}

/* Cambiar al tema de tu aplicación */
#form-cache-indicator {
    background: linear-gradient(135deg, #1962bc 0%, #144a91 100%) !important;
}
```

## 🔒 Seguridad y Privacidad

### ¿Qué NO se guarda automáticamente?

1. **Campos de tipo `password`**: Excluidos automáticamente
2. **Campos de tipo `file`**: No se pueden guardar en localStorage
3. **Campos en la lista `excludeFields`**: Los que especifiques
4. **Tokens CSRF**: Regenerados en cada carga

### ¿Dónde se guardan los datos?

- **LocalStorage del navegador**: Los datos quedan en el dispositivo del usuario
- **No se envían al servidor**: Solo se guardan localmente
- **Por dominio**: Cada dominio tiene su propio storage
- **Límite**: ~5-10MB según navegador

### Recomendaciones de seguridad

```javascript
// ✅ BIEN: Excluir datos sensibles
new FormCache('payment_form', {
    excludeFields: [
        'card_number',
        'cvv',
        'pin',
        'social_security',
        'password'
    ]
});

// ❌ MAL: Guardar todo incluyendo datos sensibles
new FormCache('payment_form');
```

## 🧪 Pruebas y Depuración

### Activar modo debug

```html
<form id="test_form" data-cache="true" data-cache-debug="true">
```

O programáticamente:

```javascript
const cache = new FormCache('test_form', { debug: true });
```

Verás en la consola:
```
[FormCache test_form] Inicializado
[FormCache test_form] Guardado automático exitoso {nombre: "Juan", email: "juan@example.com"}
[FormCache test_form] Datos restaurados desde cache {...}
```

### Ver datos en localStorage

```javascript
// En la consola del navegador
localStorage.getItem('form_cache_mi_formulario')

// Ver todo el localStorage
console.table(localStorage)

// Limpiar manualmente
localStorage.removeItem('form_cache_mi_formulario')
```

### Probar funcionalidad

1. Llena algunos campos del formulario
2. Espera 1-2 segundos (verás notificación de guardado)
3. Recarga la página (F5)
4. Los datos deberían restaurarse automáticamente
5. Verás notificación azul indicando "Datos restaurados"

## 🐛 Solución de Problemas

### Los datos no se guardan

**Verificar:**
```javascript
// 1. ¿Está incluido el script?
console.log(typeof FormCache); // Debe ser 'function'

// 2. ¿El formulario tiene ID?
document.getElementById('mi_formulario'); // No debe ser null

// 3. ¿Está activado?
// Verificar que el form tenga data-cache="true"

// 4. ¿Hay errores en consola?
// Revisar la consola del navegador (F12)
```

### Los datos no se restauran

```javascript
// Verificar si existe cache
const cache = new FormCache('mi_formulario');
console.log(cache.hasCache()); // Debe ser true

// Ver contenido del cache
console.log(cache.getCacheInfo());

// Verificar localStorage
console.log(localStorage.getItem('form_cache_mi_formulario'));
```

### Límite de almacenamiento excedido

```javascript
// Limpiar caches antiguos
Object.keys(localStorage)
    .filter(key => key.startsWith('form_cache_'))
    .forEach(key => {
        const data = JSON.parse(localStorage.getItem(key));
        const date = new Date(data.timestamp);
        const daysSince = (Date.now() - date) / (1000 * 60 * 60 * 24);
        
        // Eliminar si tiene más de 7 días
        if (daysSince > 7) {
            localStorage.removeItem(key);
            console.log(`Limpiado: ${key}`);
        }
    });
```

### Conflictos entre formularios

Si tienes múltiples formularios en la misma página:

```javascript
// Usar storageKey único para cada uno
new FormCache('form1', { storageKey: 'mi_app_form_contacto' });
new FormCache('form2', { storageKey: 'mi_app_form_registro' });
```

## 📊 Formularios Ya Configurados

En Gerontología App, estos formularios ya tienen cache activado:

✅ **Historia Gerontológica** (`historia_gerontologica.html`)
- ID: `historia_gerontologica_form`
- Intervalo: 2000ms
- Excluye: ninguno

✅ **Evolución Enfermería** (`evolucion_enfermeria.html`)
- ID: `evolucion_enfermeria_form`
- Intervalo: 1500ms
- Excluye: ninguno

✅ **Registro Usuario** (`registro.html`)
- ID: `registroForm`
- Intervalo: 1000ms
- Excluye: `contrasena`, `contrasena_confirmacion`

## 🚀 Próximos Pasos

1. **Agregar a más formularios**: Identifica formularios largos y agrégales `data-cache="true"`
2. **Monitorear uso**: Activa debug temporalmente para ver cómo se usa
3. **Ajustar tiempos**: Si el servidor es lento, aumenta `saveInterval`
4. **Personalizar notificaciones**: Ajusta colores según tu tema
5. **Añadir sincronización**: Para Empleados autenticados, podrías enviar el cache al servidor

## 📞 Soporte

Para dudas o problemas:
- Revisa la consola del navegador (F12)
- Activa modo debug: `data-cache-debug="true"`
- Verifica que el script esté cargado correctamente
- Consulta los ejemplos en este documento

---

**Última actualización**: Enero 2026  
**Versión**: 1.0  
**Autor**: Gerontología App Development Team
