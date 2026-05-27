import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from myapp.models import Identificacion, EvolucionDiariaEnfermeria
from django.contrib.auth.models import User
from datetime import date

print("\n" + "="*70)
print("PRUEBA DE GUARDADO DE EVOLUCIÓN DE ENFERMERÍA")
print("="*70)

# Verificar que hay Usuarios
Usuarios = Identificacion.objects.all()
print(f"\n✓ Usuarios disponibles: {Usuarios.count()}")

if Usuarios.count() > 0:
    paciente = Usuarios.first()
    print(f"  - Paciente de prueba: {paciente.primer_nombre} {paciente.primer_apellido}")
    
    # Verificar usuario de enfermería
    usuario = User.objects.filter(groups__name='Enfermeria').first()
    if usuario:
        print(f"\n✓ Usuario de enfermería: {usuario.username}")
        
        # Intentar crear un registro de prueba
        try:
            evolucion = EvolucionDiariaEnfermeria.objects.create(
                paciente=paciente,
                fecha=date.today(),
                paso_el_dia='B',
                alimentacion='B',
                elimina='B',
                exonera='B',
                medicamentos='1',
                frecuencia_cardiaca='72',
                presion_arterial='120/80',
                temperatura='36.5',
                frecuencia_respiratoria='18',
                novedad='0',
                observacion='Prueba de guardado',
                nombre_profesional=f'{usuario.first_name} {usuario.last_name}',
                identificacion_profesional='123456',
                firma='Firma de prueba',
                usuario_registro=usuario
            )
            print(f"\n✓ Registro de evolución creado exitosamente!")
            print(f"  - ID: {evolucion.id}")
            print(f"  - Fecha: {evolucion.fecha}")
            print(f"  - Paciente: {evolucion.paciente.primer_nombre} {evolucion.paciente.primer_apellido}")
            print(f"  - Profesional: {evolucion.nombre_profesional}")
            
            # Verificar que se guardó
            verificar = EvolucionDiariaEnfermeria.objects.filter(id=evolucion.id).first()
            if verificar:
                print(f"\n✓ Verificación: El registro SÍ quedó guardado en la base de datos")
            else:
                print(f"\n✗ Error: El registro NO se encontró en la base de datos")
                
        except Exception as e:
            print(f"\n✗ Error al crear registro: {str(e)}")
    else:
        print("\n✗ No se encontró ningún usuario de enfermería")
else:
    print("\n✗ No hay Usuarios registrados para hacer la prueba")

# Mostrar últimas evoluciones
print("\n" + "="*70)
print("ÚLTIMAS EVOLUCIONES REGISTRADAS")
print("="*70)

evoluciones = EvolucionDiariaEnfermeria.objects.all().order_by('-fecha_registro')[:5]
print(f"\nTotal de evoluciones en la BD: {EvolucionDiariaEnfermeria.objects.count()}")

if evoluciones:
    for i, ev in enumerate(evoluciones, 1):
        print(f"\n{i}. Fecha: {ev.fecha}")
        print(f"   Paciente: {ev.paciente.primer_nombre} {ev.paciente.primer_apellido}")
        print(f"   Pasó el día: {ev.paso_el_dia}")
        print(f"   Profesional: {ev.nombre_profesional}")
        print(f"   Registrado: {ev.fecha_registro}")
else:
    print("\nNo hay evoluciones registradas aún.")

print("\n" + "="*70)
