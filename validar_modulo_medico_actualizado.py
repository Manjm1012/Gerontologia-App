"""
Script para validar las correcciones en el módulo médico
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User
from myapp.models import Identificacion, ConsultaMedica, EvolucionDiariaEnfermeria, FamiliaAcudientes

print("=" * 60)
print("VALIDACIÓN DEL MÓDULO MÉDICO")
print("=" * 60)

# 1. Verificar usuario médico
print("\n1. Verificando usuario médico...")
try:
    medico = User.objects.get(username='medico1')
    print(f"   ✓ Usuario médico encontrado: {medico.username}")
    print(f"   ✓ Grupos: {', '.join([g.name for g in medico.groups.all()])}")
except User.DoesNotExist:
    print("   ✗ Usuario médico no encontrado")

# 2. Verificar Usuarios
print("\n2. Verificando Usuarios...")
total_Usuarios = Identificacion.objects.count()
print(f"   ✓ Total de Usuarios: {total_Usuarios}")

if total_Usuarios > 0:
    paciente = Identificacion.objects.first()
    print(f"   ✓ Primer paciente: {paciente.primer_nombre} {paciente.primer_apellido} (ID: {paciente.id})")
    
    # 3. Verificar consultas médicas del paciente
    print("\n3. Verificando consultas médicas...")
    consultas = ConsultaMedica.objects.filter(paciente=paciente)
    print(f"   ✓ Consultas del paciente {paciente.primer_nombre}: {consultas.count()}")
    
    # 4. Verificar evoluciones de enfermería del paciente
    print("\n4. Verificando evoluciones de enfermería...")
    evoluciones = EvolucionDiariaEnfermeria.objects.filter(paciente=paciente)
    print(f"   ✓ Evoluciones del paciente {paciente.primer_nombre}: {evoluciones.count()}")
    
    # 5. Verificar acudiente
    print("\n5. Verificando acudientes...")
    try:
        acudiente = FamiliaAcudientes.objects.filter(paciente=paciente).first()
        if acudiente:
            print(f"   ✓ Acudiente: {acudiente.acudiente_nombre}")
        else:
            print(f"   - Sin acudiente registrado")
    except:
        print("   - Sin acudiente registrado")

# 6. Verificar todas las consultas médicas
print("\n6. Verificando todas las consultas médicas...")
todas_consultas = ConsultaMedica.objects.all()
print(f"   ✓ Total de consultas médicas: {todas_consultas.count()}")

print("\n" + "=" * 60)
print("VALIDACIÓN COMPLETADA")
print("=" * 60)
print("\n📋 URLs disponibles:")
print("   - Módulo Médico: http://127.0.0.1:8000/medico/")
print("   - Nueva Consulta: http://127.0.0.1:8000/medico/consulta-nueva/")
print("   - Nuevo Enunciado: http://127.0.0.1:8000/medico/enunciado-nuevo/")
if total_Usuarios > 0:
    print(f"   - Ver Historial Paciente: http://127.0.0.1:8000/paciente/{paciente.id}/")
print("\n💡 Credenciales: medico1 / Medico123")
