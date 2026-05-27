from django.contrib import admin
from .models import Usuario, EvolucionDiariaEnfermeria, Identificacion,ConsultaMedica,EnunciadoMedico


# Register your models here.
# Este metodo permite acceder a las tablas desde el panel de administración de Django.
admin.site.register(Usuario)

# Registro del modelo de Evolución Diaria de Enfermería
@admin.register(EvolucionDiariaEnfermeria)
class EvolucionDiariaEnfermeriaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'get_paciente_nombre', 'paso_el_dia', 'novedad', 'nombre_profesional', 'fecha_registro']
    list_filter = ['fecha', 'paso_el_dia', 'novedad']
    search_fields = ['paciente__primer_nombre', 'paciente__primer_apellido', 'nombre_profesional', 'observacion']
    date_hierarchy = 'fecha'
    readonly_fields = ['fecha_registro', 'usuario_registro']
    
    def get_paciente_nombre(self, obj):
        return f"{obj.paciente.primer_nombre} {obj.paciente.primer_apellido}"
    get_paciente_nombre.short_description = 'Paciente'

# Registro del modelo Identificacion si no está registrado
if not admin.site.is_registered(Identificacion):
    admin.site.register(Identificacion) 

    
# ============================
# Consulta médica (módulo del médico)
# ============================

@admin.register(ConsultaMedica)
class ConsultaMedicaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'paciente', 'medico']
    list_filter = ['fecha', 'medico']
    search_fields = [
        'paciente__primer_nombre',
        'paciente__primer_apellido',
        'motivo_consulta',
        'diagnostico',
    ]


# ============================
# Enunciados del médico
# ============================

@admin.register(EnunciadoMedico)
class EnunciadoMedicoAdmin(admin.ModelAdmin):
    list_display = ['medico', 'fecha_registro']
    list_filter = ['fecha_registro', 'medico']
    search_fields = ['medico__first_name', 'medico__last_name', 'texto']


