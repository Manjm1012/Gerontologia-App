/**
 * Sistema de Cache Automático para Formularios
 * Guarda automáticamente los datos en localStorage mientras el usuario llena el formulario
 * Restaura los datos si la página se recarga
 * =====================================================================
 */

class FormCache {
    constructor(formId, options = {}) {
        this.formId = formId;
        this.form = document.getElementById(formId);
        
        // Opciones configurables
        this.options = {
            storageKey: options.storageKey || `form_cache_${formId}`,
            saveInterval: options.saveInterval || 1000, // ms entre guardados automáticos
            showNotification: options.showNotification !== false,
            clearOnSubmit: options.clearOnSubmit !== false,
            excludeFields: options.excludeFields || [], // Campos a excluir (ej: contraseñas)
            debug: options.debug || false
        };
        
        this.saveTimeout = null;
        this.lastSaved = null;
        
        if (this.form) {
            this.init();
        } else {
            console.warn(`Formulario con id "${formId}" no encontrado`);
        }
    }
    
    init() {
        // Restaurar datos guardados
        this.loadFromCache();
        
        // Configurar auto-guardado
        this.setupAutoSave();
        
        // Limpiar cache al enviar exitosamente
        if (this.options.clearOnSubmit) {
            this.form.addEventListener('submit', (e) => {
                // Solo limpiar si no hay errores de validación
                if (this.form.checkValidity()) {
                    this.clearCache();
                }
            });
        }
        
        // Mostrar indicador si hay datos guardados
        if (this.hasCache()) {
            this.showRestoreNotification();
        }
        
        this.log('Inicializado');
    }
    
    setupAutoSave() {
        // Escuchar cambios en todos los campos del formulario
        const fields = this.form.querySelectorAll('input, select, textarea');
        
        fields.forEach(field => {
            // Excluir campos especificados
            if (this.options.excludeFields.includes(field.name)) {
                return;
            }
            
            // Excluir automáticamente campos de tipo password
            if (field.type === 'password') {
                return;
            }
            
            // Eventos para diferentes tipos de campos
            if (field.type === 'checkbox' || field.type === 'radio') {
                field.addEventListener('change', () => this.scheduleSave());
            } else if (field.tagName === 'SELECT') {
                field.addEventListener('change', () => this.scheduleSave());
            } else {
                // Input text, textarea, etc.
                field.addEventListener('input', () => this.scheduleSave());
                field.addEventListener('blur', () => this.scheduleSave());
            }
        });
    }
    
    scheduleSave() {
        // Debounce: esperar un poco antes de guardar para no hacerlo en cada tecla
        clearTimeout(this.saveTimeout);
        this.saveTimeout = setTimeout(() => {
            this.saveToCache();
        }, this.options.saveInterval);
    }
    
    saveToCache() {
        const formData = {};
        const fields = this.form.querySelectorAll('input, select, textarea');
        
        fields.forEach(field => {
            // Excluir campos
            if (this.options.excludeFields.includes(field.name) || field.type === 'password') {
                return;
            }
            
            const name = field.name || field.id;
            if (!name) return;
            
            // Guardar según el tipo de campo
            if (field.type === 'checkbox') {
                formData[name] = field.checked;
            } else if (field.type === 'radio') {
                if (field.checked) {
                    formData[name] = field.value;
                }
            } else if (field.type === 'file') {
                // No guardar archivos (no se pueden almacenar en localStorage)
                return;
            } else {
                formData[name] = field.value;
            }
        });
        
        try {
            const cacheData = {
                data: formData,
                timestamp: new Date().toISOString(),
                url: window.location.pathname
            };
            
            localStorage.setItem(this.options.storageKey, JSON.stringify(cacheData));
            this.lastSaved = new Date();
            this.log('Guardado automático exitoso', formData);
            
            // Mostrar indicador temporal
            if (this.options.showNotification) {
                this.showSaveIndicator();
            }
        } catch (e) {
            console.error('Error al guardar en cache:', e);
            if (e.name === 'QuotaExceededError') {
                this.showError('El almacenamiento está lleno. Los cambios no se guardaron automáticamente.');
            }
        }
    }
    
    loadFromCache() {
        try {
            const cached = localStorage.getItem(this.options.storageKey);
            if (!cached) return;
            
            const cacheData = JSON.parse(cached);
            const formData = cacheData.data;
            
            // Restaurar valores
            Object.keys(formData).forEach(name => {
                const field = this.form.querySelector(`[name="${name}"], [id="${name}"]`);
                if (!field) return;
                
                const value = formData[name];
                
                if (field.type === 'checkbox') {
                    field.checked = value === true;
                } else if (field.type === 'radio') {
                    if (field.value === value) {
                        field.checked = true;
                    }
                } else if (field.tagName === 'SELECT') {
                    field.value = value;
                } else {
                    field.value = value || '';
                }
                
                // Disparar evento change para actualizar cualquier lógica dependiente
                field.dispatchEvent(new Event('change', { bubbles: true }));
            });
            
            this.log('Datos restaurados desde cache', formData);
        } catch (e) {
            console.error('Error al cargar desde cache:', e);
        }
    }
    
    hasCache() {
        return localStorage.getItem(this.options.storageKey) !== null;
    }
    
    clearCache() {
        localStorage.removeItem(this.options.storageKey);
        this.log('Cache limpiado');
    }
    
    getCacheInfo() {
        try {
            const cached = localStorage.getItem(this.options.storageKey);
            if (!cached) return null;
            
            const cacheData = JSON.parse(cached);
            return {
                timestamp: cacheData.timestamp,
                url: cacheData.url,
                fieldsCount: Object.keys(cacheData.data).length
            };
        } catch (e) {
            return null;
        }
    }
    
    showSaveIndicator() {
        // Buscar o crear indicador
        let indicator = document.getElementById('form-cache-indicator');
        
        if (!indicator) {
            indicator = document.createElement('div');
            indicator.id = 'form-cache-indicator';
            indicator.style.cssText = `
                position: fixed;
                bottom: 20px;
                right: 20px;
                background: #10b981;
                color: white;
                padding: 12px 20px;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                font-size: 14px;
                font-weight: 500;
                z-index: 10000;
                opacity: 0;
                transition: opacity 0.3s ease;
                display: flex;
                align-items: center;
                gap: 8px;
            `;
            indicator.innerHTML = '<i class="fas fa-check-circle"></i> <span>Guardado automáticamente</span>';
            document.body.appendChild(indicator);
        }
        
        // Mostrar
        indicator.style.opacity = '1';
        
        // Ocultar después de 2 segundos
        setTimeout(() => {
            indicator.style.opacity = '0';
        }, 2000);
    }
    
    showRestoreNotification() {
        const info = this.getCacheInfo();
        if (!info) return;
        
        const notification = document.createElement('div');
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: #1962bc;
            color: white;
            padding: 16px 24px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            font-size: 14px;
            z-index: 10001;
            display: flex;
            align-items: center;
            gap: 12px;
            max-width: 500px;
        `;
        
        const savedDate = new Date(info.timestamp);
        const timeAgo = this.getTimeAgo(savedDate);
        
        notification.innerHTML = `
            <i class="fas fa-info-circle" style="font-size: 20px;"></i>
            <div style="flex: 1;">
                <strong>Datos restaurados</strong><br>
                <small>Guardado hace ${timeAgo} (${info.fieldsCount} campos)</small>
            </div>
            <button id="clear-cache-btn" style="
                background: white;
                color: #1962bc;
                border: none;
                padding: 6px 12px;
                border-radius: 4px;
                cursor: pointer;
                font-weight: 600;
                font-size: 12px;
            ">
                Limpiar
            </button>
            <button id="close-notification-btn" style="
                background: transparent;
                border: none;
                color: white;
                cursor: pointer;
                font-size: 18px;
                padding: 0;
                width: 24px;
                height: 24px;
            ">×</button>
        `;
        
        document.body.appendChild(notification);
        
        // Botón limpiar
        notification.querySelector('#clear-cache-btn').addEventListener('click', () => {
            if (confirm('¿Deseas limpiar los datos guardados y empezar de nuevo?')) {
                this.clearCache();
                location.reload();
            }
        });
        
        // Botón cerrar
        notification.querySelector('#close-notification-btn').addEventListener('click', () => {
            notification.remove();
        });
        
        // Auto-cerrar después de 10 segundos
        setTimeout(() => {
            if (notification.parentNode) {
                notification.style.opacity = '0';
                notification.style.transition = 'opacity 0.3s ease';
                setTimeout(() => notification.remove(), 300);
            }
        }, 10000);
    }
    
    showError(message) {
        const error = document.createElement('div');
        error.style.cssText = `
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #dc2626;
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            font-size: 14px;
            z-index: 10000;
        `;
        error.textContent = message;
        document.body.appendChild(error);
        
        setTimeout(() => error.remove(), 5000);
    }
    
    getTimeAgo(date) {
        const seconds = Math.floor((new Date() - date) / 1000);
        
        if (seconds < 60) return `${seconds} segundos`;
        if (seconds < 3600) return `${Math.floor(seconds / 60)} minutos`;
        if (seconds < 86400) return `${Math.floor(seconds / 3600)} horas`;
        return `${Math.floor(seconds / 86400)} días`;
    }
    
    log(...args) {
        if (this.options.debug) {
            console.log(`[FormCache ${this.formId}]`, ...args);
        }
    }
}

// Inicialización automática para formularios con atributo data-cache
document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('form[data-cache="true"]');
    
    forms.forEach(form => {
        const options = {
            saveInterval: parseInt(form.dataset.cacheInterval) || 1000,
            showNotification: form.dataset.cacheNotification !== 'false',
            clearOnSubmit: form.dataset.cacheClearOnSubmit !== 'false',
            debug: form.dataset.cacheDebug === 'true'
        };
        
        // Excluir campos especificados
        if (form.dataset.cacheExclude) {
            options.excludeFields = form.dataset.cacheExclude.split(',').map(s => s.trim());
        }
        
        new FormCache(form.id, options);
    });
});

// Exportar para uso manual
window.FormCache = FormCache;
