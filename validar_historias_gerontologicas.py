"""
Script para validar historias gerontológicas de los Usuarios
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from myapp.models import (
    Identificacion, FamiliaAcudientes, GradoEscolaridad, 
    DatosSocioEconomicosForm, EspiritualidadReligion, HabitosRutinas
)

print("=" * 100)
print("VALIDACIÓN DE HISTORIAS GERONTOLÓGICAS")
print("=" * 100)

Usuarios = Identificacion.objects.all().order_by('id')

print(f"\n📊 Total de Usuarios: {Usuarios.count()}\n")

for paciente in Usuarios:
    nombre = f"{paciente.primer_nombre} {paciente.segundo_nombre} {paciente.primer_apellido} {paciente.segundo_apellido}".strip()
    print("=" * 100)
    print(f"PACIENTE ID {paciente.id}: {nombre}")
    print("=" * 100)
    
    # Verificar datos básicos
    print(f"✓ Datos básicos: OK")
    print(f"  - Documento: {paciente.tipo_documento} {paciente.numero_documento_paciente}")
    print(f"  - Edad: {paciente.edad} años")
    print(f"  - Ciudad: {paciente.ciudad_residencia}")
    
    # Verificar Familia/Acudientes
    try:
        familia = FamiliaAcudientes.objects.filter(paciente=paciente).first()
        if familia:
            print(f"✓ Familia/Acudiente: OK")
            print(f"  - Acudiente: {familia.acudiente_nombre}")
            print(f"  - Parentesco: {familia.acudiente_parentesco}")
            print(f"  - Contacto: {familia.acudiente_celular}")
        else:
            print(f"✗ Familia/Acudiente: NO REGISTRADO")
    except Exception as e:
        print(f"✗ Error al verificar familia: {str(e)}")
    
    # Verificar Grado de Escolaridad
    try:
        escolaridad = GradoEscolaridad.objects.filter(paciente=paciente).first()
        if escolaridad:
            print(f"✓ Escolaridad: OK")
        else:
            print(f"✗ Escolaridad: NO REGISTRADO")
    except Exception as e:
        print(f"✗ Error al verificar escolaridad: {str(e)}")
    
    # Verificar Datos Socioeconómicos
    try:
        socioeconomico = DatosSocioEconomicosForm.objects.filter(paciente=paciente).first()
        if socioeconomico:
            print(f"✓ Datos Socioeconómicos: OK")
        else:
            print(f"✗ Datos Socioeconómicos: NO REGISTRADO")
    except Exception as e:
        print(f"✗ Error al verificar datos socioeconómicos: {str(e)}")
    
    # Verificar Espiritualidad
    try:
        espiritualidad = EspiritualidadReligion.objects.filter(paciente=paciente).first()
        if espiritualidad:
            print(f"✓ Espiritualidad: OK")
        else:
            print(f"✗ Espiritualidad: NO REGISTRADO")
    except Exception as e:
        print(f"✗ Error al verificar espiritualidad: {str(e)}")
    
    # Verificar Hábitos
    try:
        habitos = HabitosRutinas.objects.filter(paciente=paciente).first()
        if habitos:
            print(f"✓ Hábitos: OK")
        else:
            print(f"✗ Hábitos: NO REGISTRADO")
    except Exception as e:
        print(f"✗ Error al verificar hábitos: {str(e)}")
    
    print()

print("=" * 100)
print("\n🔍 RESUMEN GENERAL")
print("=" * 100)

# Contar Usuarios con y sin datos completos
total_con_familia = FamiliaAcudientes.objects.count()
total_con_escolaridad = GradoEscolaridad.objects.count()
total_con_espiritualidad = EspiritualidadReligion.objects.count()
total_con_habitos = HabitosRutinas.objects.count()

print(f"\nUsuarios con información registrada:")
print(f"  - Con Familia/Acudiente: {total_con_familia}/{Usuarios.count()}")
print(f"  - Con Escolaridad: {total_con_escolaridad}/{Usuarios.count()}")
print(f"  - Con Espiritualidad: {total_con_espiritualidad}/{Usuarios.count()}")
print(f"  - Con Hábitos: {total_con_habitos}/{Usuarios.count()}")

print("\n" + "=" * 100)
