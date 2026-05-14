#!/usr/bin/env python
"""
Script para crear historias gerontológicas de prueba
Crea todas las instancias relacionadas y vincula a pacientes existentes
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from myapp.models import (
    Identificacion, HistoriaGerontologica, FamiliaAcudientes,
    GradoEscolaridad, DatosSocioEconomicosForm, TipoFamilia,
    SeguridadSocialSalud, RelacionesIntrafamiliares, ProteccionExequial,
    EspiritualidadReligion, HabitosRutinas, AspectosFisicosSalud
)

# Obtener pacientes existentes
pacientes = Identificacion.objects.all()
print(f"Encontrados {pacientes.count()} pacientes")

for paciente in pacientes:
    # Evitar duplicados
    if HistoriaGerontologica.objects.filter(fk_identificacion=paciente).exists():
        print(f"  ✓ {paciente.primer_nombre} - Ya tiene historia")
        continue
    
    # Crear todas las instancias relacionadas
    familia, _ = FamiliaAcudientes.objects.get_or_create(
        paciente=paciente,
        defaults={'telefono_acudiente': 'N/A', 'nombre_acudiente': 'No especificado'}
    )
    
    escolaridad, _ = GradoEscolaridad.objects.get_or_create(
        paciente=paciente,
        defaults={'grado_escolaridad': 'No especificado'}
    )
    
    socio, _ = DatosSocioEconomicosForm.objects.get_or_create(
        paciente=paciente,
        defaults={'ocupacion_actual': 'N/A'}
    )
    
    tipo_fam, _ = TipoFamilia.objects.get_or_create(
        paciente=paciente,
        defaults={'tipo_familia': 'N/A'}
    )
    
    seguridad, _ = SeguridadSocialSalud.objects.get_or_create(
        paciente=paciente,
        defaults={'tipo_seguro': 'No especificado'}
    )
    
    relaciones, _ = RelacionesIntrafamiliares.objects.get_or_create(
        paciente=paciente,
        defaults={'tipo_relacion': 'N/A'}
    )
    
    proteccion, _ = ProteccionExequial.objects.get_or_create(
        paciente=paciente,
        defaults={'estado_proteccion': 'No'}
    )
    
    espiritualidad, _ = EspiritualidadReligion.objects.get_or_create(
        paciente=paciente,
        defaults={'religion': 'No especificada'}
    )
    
    habitos, _ = HabitosRutinas.objects.get_or_create(
        paciente=paciente,
        defaults={'rutina_diaria': 'No especificada'}
    )
    
    aspectos, _ = AspectosFisicosSalud.objects.get_or_create(
        paciente=paciente,
        defaults={'estado_fisico': 'No especificado'}
    )
    
    # Crear la historia
    historia, created = HistoriaGerontologica.objects.get_or_create(
        fk_identificacion=paciente,
        defaults={
            'fk_familia_acudientes': familia,
            'fk_grado_escolaridad': escolaridad,
            'fk_datos_socio_economicos': socio,
            'fk_tipo_familia': tipo_fam,
            'fk_seguridad_social_salud': seguridad,
            'fk_relaciones_intrafamiliares': relaciones,
            'fk_proteccion_exequial': proteccion,
            'fk_espiritualidad_religion': espiritualidad,
            'fk_habitos_rutinas': habitos,
            'fk_aspectos_fisicos_salud': aspectos,
        }
    )
    
    if created:
        print(f"  ✓ {paciente.primer_nombre} - Historia creada")
    else:
        print(f"  ✓ {paciente.primer_nombre} - Historia existente")

print("\n✅ Historias de prueba creadas exitosamente")
print(f"Total historias: {HistoriaGerontologica.objects.count()}")
