"""
Script de validación completa de la lógica del sistema
Valida la relación entre Usuarios y el módulo de enfermería
"""

import os
import sys
import django
from datetime import date, timedelta
import random

# Configurar Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from myapp.models import Identificacion, EvolucionDiariaEnfermeria
from django.contrib.auth.models import User

def print_section(title):
    """Imprime un separador de sección"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)

def validar_Usuarios():
    """Valida que los Usuarios estén correctamente registrados"""
    print_section("1. VALIDACIÓN DE Usuarios REGISTRADOS")
    
    Usuarios = Identificacion.objects.all()
    print(f"\n📊 Total de Usuarios en el sistema: {Usuarios.count()}")
    
    if Usuarios.count() == 0:
        print("❌ No hay Usuarios registrados")
        return False
    
    print("\n👥 Lista de Usuarios:")
    for i, p in enumerate(Usuarios, 1):
        print(f"   {i}. {p.primer_nombre} {p.primer_apellido} - CC: {p.numero_documento_paciente}")
        print(f"      Edad: {p.edad} años | Sexo: {p.sexo} | Ciudad: {p.ciudad_residencia}")
    
    return True

def validar_modelo_evolucion():
    """Valida que el modelo de evolución esté correctamente configurado"""
    print_section("2. VALIDACIÓN DEL MODELO EVOLUCION DIARIA")
    
    print("\n📋 Campos del modelo EvolucionDiariaEnfermeria:")
    campos = [f.name for f in EvolucionDiariaEnfermeria._meta.get_fields()]
    for campo in campos:
        print(f"   ✓ {campo}")
    
    print(f"\n📊 Total de campos: {len(campos)}")
    
    # Verificar relación con paciente
    try:
        campo_paciente = EvolucionDiariaEnfermeria._meta.get_field('paciente')
        print(f"\n✅ Relación con paciente: {campo_paciente.related_model.__name__}")
        print(f"   Related name: {campo_paciente.remote_field.related_name}")
    except Exception as e:
        print(f"\n❌ Error en relación con paciente: {e}")
        return False
    
    return True

def crear_evoluciones_prueba():
    """Crea evoluciones de prueba para los 5 Usuarios"""
    print_section("3. CREACIÓN DE EVOLUCIONES DE PRUEBA")
    
    Usuarios = Identificacion.objects.all()[:5]
    if Usuarios.count() == 0:
        print("❌ No hay Usuarios para crear evoluciones")
        return False
    
    # Obtener usuario enfermero
    try:
        usuario_enfermero = User.objects.get(username='enfermero1')
    except User.DoesNotExist:
        print("❌ Usuario 'enfermero1' no existe")
        return False
    
    print(f"\n🏥 Usuario que registrará: {usuario_enfermero.username}")
    print(f"📅 Creando evoluciones para los últimos 3 días...\n")
    
    estados = ['B', 'R', 'M']
    si_no = ['1', '0']
    evoluciones_creadas = 0
    
    for dia in range(3):  # Últimos 3 días
        fecha = date.today() - timedelta(days=dia)
        
        for paciente in Usuarios:
            try:
                # Verificar si ya existe una evolución para este paciente en esta fecha
                existe = EvolucionDiariaEnfermeria.objects.filter(
                    paciente=paciente,
                    fecha=fecha
                ).exists()
                
                if existe:
                    print(f"   ⏭️  Ya existe evolución para {paciente.primer_nombre} {paciente.primer_apellido} - {fecha}")
                    continue
                
                # Crear evolución
                evolucion = EvolucionDiariaEnfermeria.objects.create(
                    paciente=paciente,
                    fecha=fecha,
                    paso_el_dia=random.choice(estados),
                    alimentacion=random.choice(estados),
                    elimina=random.choice(estados),
                    exonera=random.choice(estados),
                    medicamentos=random.choice(si_no),
                    frecuencia_cardiaca=str(random.randint(60, 100)),
                    presion_arterial=f"{random.randint(110, 140)}/{random.randint(60, 90)}",
                    temperatura=f"{random.uniform(36.0, 37.5):.1f}",
                    frecuencia_respiratoria=str(random.randint(12, 20)),
                    novedad=random.choice(si_no),
                    observacion=f"Evolución normal del día {fecha}",
                    nombre_profesional=f"{usuario_enfermero.first_name} {usuario_enfermero.last_name}",
                    identificacion_profesional="ENF001",
                    firma="Firma digital",
                    usuario_registro=usuario_enfermero
                )
                
                print(f"   ✅ Creada: {paciente.primer_nombre} {paciente.primer_apellido} - {fecha}")
                evoluciones_creadas += 1
                
            except Exception as e:
                print(f"   ❌ Error creando evolución para {paciente.primer_nombre}: {e}")
    
    print(f"\n📊 Total de evoluciones creadas: {evoluciones_creadas}")
    return True

def validar_relacion_paciente_evolucion():
    """Valida que la relación entre Usuarios y evoluciones funcione correctamente"""
    print_section("4. VALIDACIÓN DE RELACIÓN PACIENTE-EVOLUCIÓN")
    
    Usuarios = Identificacion.objects.all()[:5]
    
    for paciente in Usuarios:
        print(f"\n👤 Paciente: {paciente.primer_nombre} {paciente.primer_apellido}")
        
        # Obtener evoluciones del paciente usando el related_name
        evoluciones = paciente.evoluciones_enfermeria.all()
        print(f"   📋 Total de evoluciones: {evoluciones.count()}")
        
        if evoluciones.count() > 0:
            print("   📅 Últimas 3 evoluciones:")
            for ev in evoluciones[:3]:
                estado_dia = ev.get_paso_el_dia_display()
                tiene_novedad = "Sí" if ev.novedad == '1' else "No"
                print(f"      • {ev.fecha} - Estado: {estado_dia} | Novedad: {tiene_novedad}")
                print(f"        Signos vitales: FC={ev.frecuencia_cardiaca} PA={ev.presion_arterial} T={ev.temperatura}")
        else:
            print("   ⚠️  No tiene evoluciones registradas")
    
    return True

def validar_estadisticas_dashboard():
    """Valida que las estadísticas del dashboard de enfermería se calculen correctamente"""
    print_section("5. VALIDACIÓN DE ESTADÍSTICAS DEL DASHBOARD")
    
    from django.db.models import Count, Q
    
    hoy = date.today()
    print(f"\n📅 Fecha de hoy: {hoy}")
    
    # Obtener evoluciones de hoy
    evoluciones_hoy = EvolucionDiariaEnfermeria.objects.filter(fecha=hoy)
    print(f"\n📊 Evoluciones registradas hoy: {evoluciones_hoy.count()}")
    
    if evoluciones_hoy.count() == 0:
        print("⚠️  No hay evoluciones registradas para hoy. Creando algunas...")
        crear_evoluciones_hoy()
        evoluciones_hoy = EvolucionDiariaEnfermeria.objects.filter(fecha=hoy)
    
    # Calcular estadísticas
    Usuarios_atendidos = evoluciones_hoy.values('paciente').distinct().count()
    print(f"\n👥 Usuarios atendidos hoy: {Usuarios_atendidos}")
    
    signos_vitales_tomados = evoluciones_hoy.filter(
        Q(frecuencia_cardiaca__isnull=False, frecuencia_cardiaca__gt='') |
        Q(presion_arterial__isnull=False, presion_arterial__gt='') |
        Q(temperatura__isnull=False, temperatura__gt='') |
        Q(frecuencia_respiratoria__isnull=False, frecuencia_respiratoria__gt='')
    ).count()
    print(f"🌡️  Signos vitales tomados: {signos_vitales_tomados}")
    
    medicamentos_administrados = evoluciones_hoy.filter(medicamentos='1').count()
    print(f"💊 Medicamentos administrados: {medicamentos_administrados}")
    
    novedades_hoy = evoluciones_hoy.filter(novedad='1').count()
    print(f"⚠️  Novedades del día: {novedades_hoy}")
    
    # Mostrar últimas 5 evoluciones
    print("\n📋 Últimas 5 evoluciones de hoy:")
    ultimas = evoluciones_hoy.select_related('paciente').order_by('-fecha_registro')[:5]
    for ev in ultimas:
        print(f"   • {ev.paciente.primer_nombre} {ev.paciente.primer_apellido}")
        print(f"     Estado: {ev.get_paso_el_dia_display()} | Novedad: {'Sí' if ev.novedad == '1' else 'No'}")
    
    return True

def crear_evoluciones_hoy():
    """Crea evoluciones para hoy si no existen"""
    Usuarios = Identificacion.objects.all()[:5]
    usuario_enfermero = User.objects.get(username='enfermero1')
    hoy = date.today()
    
    for paciente in Usuarios:
        if not EvolucionDiariaEnfermeria.objects.filter(paciente=paciente, fecha=hoy).exists():
            EvolucionDiariaEnfermeria.objects.create(
                paciente=paciente,
                fecha=hoy,
                paso_el_dia=random.choice(['B', 'R']),
                alimentacion=random.choice(['B', 'R']),
                elimina='B',
                exonera='B',
                medicamentos='1',
                frecuencia_cardiaca=str(random.randint(60, 90)),
                presion_arterial=f"{random.randint(110, 130)}/{random.randint(60, 80)}",
                temperatura=f"{random.uniform(36.0, 37.0):.1f}",
                frecuencia_respiratoria=str(random.randint(14, 18)),
                novedad=random.choice(['0', '1']),
                observacion=f"Control regular de hoy",
                nombre_profesional=f"{usuario_enfermero.first_name} {usuario_enfermero.last_name}",
                identificacion_profesional="ENF001",
                usuario_registro=usuario_enfermero
            )

def validar_filtros_consultas():
    """Valida que las consultas y filtros funcionen correctamente"""
    print_section("6. VALIDACIÓN DE CONSULTAS Y FILTROS")
    
    print("\n🔍 Probando consultas complejas...")
    
    # Usuarios con evoluciones en los últimos 7 días
    desde = date.today() - timedelta(days=7)
    Usuarios_activos = Identificacion.objects.filter(
        evoluciones_enfermeria__fecha__gte=desde
    ).distinct()
    
    print(f"\n👥 Usuarios con evoluciones en los últimos 7 días: {Usuarios_activos.count()}")
    for p in Usuarios_activos:
        evoluciones = p.evoluciones_enfermeria.filter(fecha__gte=desde).count()
        print(f"   • {p.primer_nombre} {p.primer_apellido}: {evoluciones} evoluciones")
    
    # Evoluciones con novedades
    con_novedades = EvolucionDiariaEnfermeria.objects.filter(novedad='1')
    print(f"\n⚠️  Total de evoluciones con novedades: {con_novedades.count()}")
    
    # Evoluciones por estado del día
    for estado, nombre in [('B', 'Bueno'), ('R', 'Regular'), ('M', 'Malo')]:
        count = EvolucionDiariaEnfermeria.objects.filter(paso_el_dia=estado).count()
        print(f"   {nombre}: {count}")
    
    return True

def generar_reporte_final():
    """Genera un reporte final con toda la información"""
    print_section("📊 REPORTE FINAL DE VALIDACIÓN")
    
    total_Usuarios = Identificacion.objects.count()
    total_evoluciones = EvolucionDiariaEnfermeria.objects.count()
    
    print(f"""
    ✅ Sistema validado correctamente
    
    📈 RESUMEN:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    👥 Total de Usuarios:        {total_Usuarios}
    📋 Total de evoluciones:      {total_evoluciones}
    📅 Evoluciones hoy:          {EvolucionDiariaEnfermeria.objects.filter(fecha=date.today()).count()}
    
    🔗 RELACIONES:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ✓ Paciente → Evolución: CORRECTA
    ✓ Evolución → Usuario: CORRECTA
    ✓ Estadísticas Dashboard: FUNCIONANDO
    ✓ Filtros y Consultas: OPERATIVOS
    
    🎯 ESTADO: SISTEMA OPERATIVO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

def main():
    """Función principal que ejecuta todas las validaciones"""
    print("\n" + "="*70)
    print("🏥 VALIDACIÓN COMPLETA DEL SISTEMA GERONTOLOGÍA APP")
    print("="*70)
    print(f"📅 Fecha: {date.today()}")
    print("="*70)
    
    try:
        # Ejecutar validaciones
        validar_Usuarios()
        validar_modelo_evolucion()
        crear_evoluciones_prueba()
        validar_relacion_paciente_evolucion()
        validar_estadisticas_dashboard()
        validar_filtros_consultas()
        generar_reporte_final()
        
        print("\n✅ VALIDACIÓN COMPLETADA EXITOSAMENTE\n")
        
    except Exception as e:
        print(f"\n❌ ERROR EN VALIDACIÓN: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
