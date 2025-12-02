// ====================================
// SCRIPTS MÓDULO DE ENFERMERÍA
// ====================================

document.addEventListener('DOMContentLoaded', function() {
    console.log('Módulo de Enfermería cargado correctamente');

    // Funcionalidad para los botones de acción en la tabla de pacientes
    const actionButtons = document.querySelectorAll('.btn-action');
    
    actionButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const action = this.classList.contains('btn-view') ? 'ver' :
                          this.classList.contains('btn-edit') ? 'editar' : 'signos vitales';
            
            // Obtener información de la fila
            const row = this.closest('tr');
            const documento = row.cells[0].textContent;
            const nombre = row.cells[1].textContent;
            
            console.log(`Acción: ${action} - Paciente: ${nombre} (${documento})`);
            
            // Aquí puedes agregar la lógica para cada acción
            // Por ejemplo, abrir un modal o redirigir a otra página
            alert(`Acción: ${action}\nPaciente: ${nombre}\nDocumento: ${documento}`);
        });
    });

    // Funcionalidad para las tarjetas de acción rápida
    const actionCards = document.querySelectorAll('.action-card');
    
    actionCards.forEach(card => {
        card.addEventListener('click', function(e) {
            const cardTitle = this.querySelector('h3').textContent;
            console.log(`Tarjeta seleccionada: ${cardTitle}`);
            
            // Aquí puedes agregar navegación específica o mostrar modales
            // Por ahora, si el href es un ancla (#), prevenimos la acción por defecto
            if (this.getAttribute('href').startsWith('#')) {
                e.preventDefault();
                alert(`Función en desarrollo: ${cardTitle}`);
            }
        });
    });

    // Actualizar hora en tiempo real (opcional)
    function actualizarHora() {
        const now = new Date();
        const options = { 
            weekday: 'long', 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        };
        const fechaHora = now.toLocaleDateString('es-ES', options);
        
        // Buscar si hay un elemento para mostrar la hora
        const horaElement = document.querySelector('.current-time');
        if (horaElement) {
            horaElement.textContent = fechaHora;
        }
    }

    // Actualizar cada minuto
    actualizarHora();
    setInterval(actualizarHora, 60000);

    // Animación de entrada para las tarjetas
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '0';
                entry.target.style.transform = 'translateY(20px)';
                
                setTimeout(() => {
                    entry.target.style.transition = 'all 0.5s ease';
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, 100);
                
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observar elementos para animación
    document.querySelectorAll('.stat-card, .action-card').forEach(card => {
        observer.observe(card);
    });

    // Confirmación para cerrar sesión
    const logoutBtn = document.querySelector('.btn-logout');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', function(e) {
            const confirmLogout = confirm('¿Está seguro que desea cerrar sesión?');
            if (!confirmLogout) {
                e.preventDefault();
            }
        });
    }
});
