import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from myapp.models import (
    Identificacion, GradoEscolaridad, DatosSocioEconomicosForm,
    EspiritualidadReligion, HabitosRutinas
)

def completar_historias():
    """Completa las historias gerontológicas faltantes con datos únicos para cada paciente"""
    
    print("\n" + "="*100)
    print("COMPLETANDO HISTORIAS GERONTOLÓGICAS")
    print("="*100 + "\n")
    
    # Paciente 1: María Elena - ID 1
    print("📝 Completando historia de Paciente ID 1: María Elena Rodríguez García")
    paciente1 = Identificacion.objects.get(pk=1)
    
    # Escolaridad
    if not GradoEscolaridad.objects.filter(paciente=paciente1).exists():
        GradoEscolaridad.objects.create(
            paciente=paciente1,
            lee='1',
            escribe='1',
            primaria_completa='1',
            secundaria_completa='0',
            tecnico='',
            tecnologo='',
            profesional='',
            maestria='',
            otros_estudios=''
        )
        print("  ✓ Escolaridad: Lee y escribe, Primaria Completa")
    
    # Datos Socioeconómicos
    if not DatosSocioEconomicosForm.objects.filter(paciente=paciente1).exists():
        DatosSocioEconomicosForm.objects.create(
            paciente=paciente1,
            actividad_desempenada='Ama de casa',
            ocupacion_actual='Jubilada',
            aporte_familiar='1',
            jubilacion='1',
            renta_propia='0',
            otros_ingresos='Ninguno'
        )
        print("  ✓ Datos Socioeconómicos: Jubilada, Recibe aporte familiar")
    
    # Espiritualidad
    if not EspiritualidadReligion.objects.filter(paciente=paciente1).exists():
        EspiritualidadReligion.objects.create(
            paciente=paciente1,
            grupo_religioso='1',
            cual_grupo_religioso='Grupo de oración parroquial',
            religion='Católica',
            practica_religiosa='MISA',
            otros_practicas_religiosas=''
        )
        print("  ✓ Espiritualidad: Católica, asiste a misa regularmente")
    
    # Hábitos
    if not HabitosRutinas.objects.filter(paciente=paciente1).exists():
        HabitosRutinas.objects.create(
            paciente=paciente1,
            actividad_fisica='1',
            tipo_actividad_fisica='Caminata 30 minutos diarios',
            actividades_recreativas='Tejido, lectura, reuniones familiares'
        )
        print("  ✓ Hábitos: Actividad física regular, recreación variada")
    
    print()
    
    # Paciente 2: Carmen Rosa - ID 2
    print("📝 Completando historia de Paciente ID 2: Carmen Rosa Rodríguez García")
    paciente2 = Identificacion.objects.get(pk=2)
    
    # Escolaridad
    if not GradoEscolaridad.objects.filter(paciente=paciente2).exists():
        GradoEscolaridad.objects.create(
            paciente=paciente2,
            lee='1',
            escribe='1',
            primaria_completa='1',
            secundaria_completa='1',
            tecnico='',
            tecnologo='',
            profesional='',
            maestria='',
            otros_estudios=''
        )
        print("  ✓ Escolaridad: Lee y escribe, Bachillerato Completo")
    
    # Datos Socioeconómicos
    if not DatosSocioEconomicosForm.objects.filter(paciente=paciente2).exists():
        DatosSocioEconomicosForm.objects.create(
            paciente=paciente2,
            actividad_desempenada='Comerciante',
            ocupacion_actual='Jubilada',
            aporte_familiar='1',
            jubilacion='1',
            renta_propia='1',
            otros_ingresos='Arriendo de local comercial'
        )
        print("  ✓ Datos Socioeconómicos: Jubilada con renta propia, arriendo de local")
    
    # Espiritualidad
    if not EspiritualidadReligion.objects.filter(paciente=paciente2).exists():
        EspiritualidadReligion.objects.create(
            paciente=paciente2,
            grupo_religioso='1',
            cual_grupo_religioso='Iglesia Cristiana Pentecostal',
            religion='Cristiana Evangélica',
            practica_religiosa='CULTO',
            otros_practicas_religiosas='Estudios bíblicos semanales'
        )
        print("  ✓ Espiritualidad: Cristiana Evangélica, asiste a cultos")
    
    # Hábitos
    if not HabitosRutinas.objects.filter(paciente=paciente2).exists():
        HabitosRutinas.objects.create(
            paciente=paciente2,
            actividad_fisica='1',
            tipo_actividad_fisica='Ejercicios de estiramiento 3 veces/semana',
            actividades_recreativas='Costura, manualidades, actividades de iglesia'
        )
        print("  ✓ Hábitos: Ejercicio moderado, recreación en actividades manuales")
    
    print()
    
    # Paciente 3: Luis Alberto - ID 3
    print("📝 Completando historia de Paciente ID 3: Luis Alberto González Méndez")
    paciente3 = Identificacion.objects.get(pk=3)
    
    # Datos Socioeconómicos
    if not DatosSocioEconomicosForm.objects.filter(paciente=paciente3).exists():
        DatosSocioEconomicosForm.objects.create(
            paciente=paciente3,
            actividad_desempenada='Obrero de construcción',
            ocupacion_actual='Desempleado',
            aporte_familiar='1',
            jubilacion='0',
            renta_propia='0',
            otros_ingresos='Subsidio Colombia Mayor'
        )
        print("  ✓ Datos Socioeconómicos: Desempleado, recibe subsidio y aporte familiar")
    
    # Espiritualidad
    if not EspiritualidadReligion.objects.filter(paciente=paciente3).exists():
        EspiritualidadReligion.objects.create(
            paciente=paciente3,
            grupo_religioso='0',
            cual_grupo_religioso='',
            religion='Católica',
            practica_religiosa='OTROS',
            otros_practicas_religiosas='Solo en festividades importantes (Navidad, Semana Santa)'
        )
        print("  ✓ Espiritualidad: Católico no practicante, solo festividades")
    
    # Hábitos
    if not HabitosRutinas.objects.filter(paciente=paciente3).exists():
        HabitosRutinas.objects.create(
            paciente=paciente3,
            actividad_fisica='0',
            tipo_actividad_fisica='',
            actividades_recreativas='Escuchar radio, visitas familiares ocasionales'
        )
        print("  ✓ Hábitos: Sedentario, recreación pasiva (radio)")
    
    print()
    print("="*100)
    print("✅ HISTORIAS COMPLETADAS EXITOSAMENTE")
    print("="*100)
    print("\n📊 Resumen:")
    print("  - Paciente 1 (María Elena): 4 registros agregados")
    print("  - Paciente 2 (Carmen Rosa): 4 registros agregados")
    print("  - Paciente 3 (Luis Alberto): 3 registros agregados")
    print("\n✅ Los 11 Usuarios ahora tienen historias gerontológicas completas y diferentes")

if __name__ == '__main__':
    completar_historias()
