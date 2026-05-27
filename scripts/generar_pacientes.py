"""
Script para generar 5 Usuarios con información diversa
Autor: Sistema Gerontología App
Fecha: Enero 2026
"""

import os
import sys
import django
from datetime import date

# Configurar Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from myapp.models import (
    Identificacion, FamiliaAcudientes, GradoEscolaridad, 
    DatosSocioEconomicosForm, TipoFamilia, SeguridadSocialSalud,
    RelacionesIntrafamiliares, ProteccionExequial, EspiritualidadReligion,
    HabitosRutinas, AspectosFisicosSalud, Medicamentos,
    AdversidadesMedicamentos, AdversidadesAlimentos, AntecedentesToxicos
)

def calcular_edad(fecha_nacimiento):
    """Calcula la edad a partir de la fecha de nacimiento"""
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def crear_paciente_1():
    """
    Paciente 1: María Elena Rodríguez García
    Mujer de 78 años, viuda, buena salud general
    """
    print("\n🔵 Creando Paciente 1: María Elena Rodríguez García...")
    
    # Identificación
    paciente = Identificacion.objects.create(
        primer_nombre="María Elena",
        segundo_nombre="",
        primer_apellido="Rodríguez",
        segundo_apellido="García",
        fecha_nacimiento=date(1948, 3, 15),
        edad=78,
        tipo_documento="CC",
        numero_documento_paciente="41234567",
        ciudad_residencia="Bogotá",
        sexo="Femenino",
        grupo_sanguineo="O+",
        pais_nacimiento="Colombia",
        departamento_nacimiento="Cundinamarca",
        ciudad_nacimiento="Bogotá",
        zona_residencia="U"
    )
    
    # Familia y Acudientes
    FamiliaAcudientes.objects.create(
        paciente=paciente,
        acudiente_nombre="Carlos Rodríguez Pérez",
        acudiente_parentesco="Hijo",
        acudiente_telefono="6012345678",
        acudiente_celular="3101234567",
        acudiente_direccion="Calle 45 # 12-34, Bogotá",
        acudiente_email="carlos.rodriguez@email.com",
        acudiente_estado_civil="C"
    )
    
    # Grado de Escolaridad
    GradoEscolaridad.objects.create(
        paciente=paciente,
        lee="1",
        escribe="1",
        primaria_completa="1",
        secundaria_completa="1",
        tecnico="",
        tecnologo="",
        profesional="Licenciada en Educación",
        maestria="",
        otros_estudios="Cursos de pedagogía"
    )
    
    # Datos Socioeconómicos
    DatosSocioEconomicosForm.objects.create(
        paciente=paciente,
        actividad_desempenada="Docente de primaria",
        ocupacion_actual="Jubilada",
        aporte_familiar="1",
        jubilacion="1",
        renta_propia="0",
        otros_ingresos=""
    )
    
    # Tipo de Familia
    TipoFamilia.objects.create(
        paciente=paciente,
        tipo_familia="FE",  # Familia Extensa
        otro_razon_tipo_familia=""
    )
    
    # Seguridad Social
    SeguridadSocialSalud.objects.create(
        paciente=paciente,
        regimen_seguridad_social="CONTRIBUTIVO",
        afiliacion_salud="Nueva EPS",
        ips="Clínica del Country"
    )
    
    # Relaciones Intrafamiliares
    RelacionesIntrafamiliares.objects.create(
        paciente=paciente,
        tipo_relacion="BUENA",
        maltrato="0",
        explicacion_relacion="Relación armoniosa con sus hijos y nietos. Participación activa en eventos familiares.",
        tipo_maltrato=""
    )
    
    # Protección Exequial
    ProteccionExequial.objects.create(
        paciente=paciente,
        proteccion_exequial="1",
        compania_proteccion_exequial="Seguros del Estado"
    )
    
    # Espiritualidad
    EspiritualidadReligion.objects.create(
        paciente=paciente,
        grupo_religioso="1",
        cual_grupo_religioso="Católica",
        religion="Católica",
        practica_religiosa="MISA",
        otros_practicas_religiosas=""
    )
    
    # Hábitos y Rutinas
    HabitosRutinas.objects.create(
        paciente=paciente,
        actividad_fisica="1",
        tipo_actividad_fisica="Caminatas diarias, yoga para adultos mayores",
        actividades_recreativas="Lectura, tejido, club de abuelos"
    )
    
    # Aspectos Físicos
    AspectosFisicosSalud.objects.create(
        paciente=paciente,
        estado_salud="BUENA",
        explicacion_estado_salud="En general presenta buen estado de salud. Control médico regular."
    )
    
    # Medicamentos
    Medicamentos.objects.create(
        paciente=paciente,
        nombre_medicamento="Losartán",
        dosis="50mg cada 24 horas",
        observaciones="Para control de presión arterial"
    )
    
    Medicamentos.objects.create(
        paciente=paciente,
        nombre_medicamento="Atorvastatina",
        dosis="20mg cada noche",
        observaciones="Control de colesterol"
    )
    
    # Adversidades a Medicamentos
    AdversidadesMedicamentos.objects.create(
        paciente=paciente,
        reacciones_adversas="0",
        descripcion_reacciones="",
        alergias_medicamentos="0",
        descripcion_alergias="",
        autprescripcion_medicamentos="0"
    )
    
    # Adversidades a Alimentos
    AdversidadesAlimentos.objects.create(
        paciente=paciente,
        adversidad_alimentos="0",
        descripcion_adversidad="",
        alergias_alimentos="0",
        descripcion_alergias_alimentos=""
    )
    
    # Antecedentes Tóxicos
    AntecedentesToxicos.objects.create(
        paciente=paciente,
        consumo_sustancias="0",
        consumo_sustancias_tabaco="0",
        consumo_sustancias_cafe="1",
        consumo_sustancias_psicoactivas="0",
        frecuencia_consumo="Diaria",
        cantidad_consumo="1 taza"
    )
    
    print(f"✅ Paciente creado: {paciente}")
    return paciente


def crear_paciente_2():
    """
    Paciente 2: José Antonio Martínez López
    Hombre de 82 años, casado, diabetes controlada
    """
    print("\n🔵 Creando Paciente 2: José Antonio Martínez López...")
    
    # Identificación
    paciente = Identificacion.objects.create(
        primer_nombre="José Antonio",
        segundo_nombre="",
        primer_apellido="Martínez",
        segundo_apellido="López",
        fecha_nacimiento=date(1944, 7, 22),
        edad=82,
        tipo_documento="CC",
        numero_documento_paciente="17345678",
        ciudad_residencia="Medellín",
        sexo="Masculino",
        grupo_sanguineo="A+",
        pais_nacimiento="Colombia",
        departamento_nacimiento="Antioquia",
        ciudad_nacimiento="Medellín",
        zona_residencia="U"
    )
    
    # Familia y Acudientes
    FamiliaAcudientes.objects.create(
        paciente=paciente,
        acudiente_nombre="Rosa María Martínez Gómez",
        acudiente_parentesco="Esposa",
        acudiente_telefono="6045678901",
        acudiente_celular="3209876543",
        acudiente_direccion="Carrera 70 # 45-23, Medellín",
        acudiente_email="rosa.martinez@email.com",
        acudiente_estado_civil="C"
    )
    
    # Grado de Escolaridad
    GradoEscolaridad.objects.create(
        paciente=paciente,
        lee="1",
        escribe="1",
        primaria_completa="1",
        secundaria_completa="1",
        tecnico="",
        tecnologo="Tecnólogo en Mecánica Industrial",
        profesional="",
        maestria="",
        otros_estudios=""
    )
    
    # Datos Socioeconómicos
    DatosSocioEconomicosForm.objects.create(
        paciente=paciente,
        actividad_desempenada="Técnico mecánico",
        ocupacion_actual="Jubilado",
        aporte_familiar="0",
        jubilacion="1",
        renta_propia="1",
        otros_ingresos="Arriendo de un local comercial"
    )
    
    # Tipo de Familia
    TipoFamilia.objects.create(
        paciente=paciente,
        tipo_familia="FN",  # Familia Nuclear
        otro_razon_tipo_familia=""
    )
    
    # Seguridad Social
    SeguridadSocialSalud.objects.create(
        paciente=paciente,
        regimen_seguridad_social="CONTRIBUTIVO",
        afiliacion_salud="Sura",
        ips="Hospital Pablo Tobón Uribe"
    )
    
    # Relaciones Intrafamiliares
    RelacionesIntrafamiliares.objects.create(
        paciente=paciente,
        tipo_relacion="BUENA",
        maltrato="0",
        explicacion_relacion="Convive con su esposa. Relación estable de 55 años de matrimonio.",
        tipo_maltrato=""
    )
    
    # Protección Exequial
    ProteccionExequial.objects.create(
        paciente=paciente,
        proteccion_exequial="1",
        compania_proteccion_exequial="Coomeva"
    )
    
    # Espiritualidad
    EspiritualidadReligion.objects.create(
        paciente=paciente,
        grupo_religioso="1",
        cual_grupo_religioso="Católico",
        religion="Católica",
        practica_religiosa="ORACION",
        otros_practicas_religiosas=""
    )
    
    # Hábitos y Rutinas
    HabitosRutinas.objects.create(
        paciente=paciente,
        actividad_fisica="1",
        tipo_actividad_fisica="Caminatas ligeras 3 veces por semana",
        actividades_recreativas="Dominó, radio, televisión"
    )
    
    # Aspectos Físicos
    AspectosFisicosSalud.objects.create(
        paciente=paciente,
        estado_salud="REGULAR",
        explicacion_estado_salud="Diabetes tipo 2 controlada con medicación. Presenta movilidad reducida."
    )
    
    # Medicamentos
    Medicamentos.objects.create(
        paciente=paciente,
        nombre_medicamento="Metformina",
        dosis="850mg cada 12 horas",
        observaciones="Control de diabetes"
    )
    
    Medicamentos.objects.create(
        paciente=paciente,
        nombre_medicamento="Enalapril",
        dosis="10mg cada 24 horas",
        observaciones="Hipertensión arterial"
    )
    
    Medicamentos.objects.create(
        paciente=paciente,
        nombre_medicamento="Aspirina",
        dosis="100mg cada 24 horas",
        observaciones="Antiagregante plaquetario"
    )
    
    # Adversidades a Medicamentos
    AdversidadesMedicamentos.objects.create(
        paciente=paciente,
        reacciones_adversas="1",
        descripcion_reacciones="Náuseas leves con Metformina al inicio del tratamiento",
        alergias_medicamentos="0",
        descripcion_alergias="",
        autprescripcion_medicamentos="0"
    )
    
    # Adversidades a Alimentos
    AdversidadesAlimentos.objects.create(
        paciente=paciente,
        adversidad_alimentos="0",
        descripcion_adversidad="",
        alergias_alimentos="0",
        descripcion_alergias_alimentos=""
    )
    
    # Antecedentes Tóxicos
    AntecedentesToxicos.objects.create(
        paciente=paciente,
        consumo_sustancias="1",
        consumo_sustancias_tabaco="0",
        consumo_sustancias_cafe="1",
        consumo_sustancias_psicoactivas="0",
        frecuencia_consumo="2/día",
        cantidad_consumo="2 tazas"
    )
    
    print(f"✅ Paciente creado: {paciente}")
    return paciente


def crear_paciente_3():
    """
    Paciente 3: Ana Lucía Gómez Torres
    Mujer de 71 años, divorciada, activa socialmente
    """
    print("\n🔵 Creando Paciente 3: Ana Lucía Gómez Torres...")
    
    # Identificación
    paciente = Identificacion.objects.create(
        primer_nombre="Ana Lucía",
        segundo_nombre="",
        primer_apellido="Gómez",
        segundo_apellido="Torres",
        fecha_nacimiento=date(1955, 11, 8),
        edad=71,
        tipo_documento="CC",
        numero_documento_paciente="51456789",
        ciudad_residencia="Cali",
        sexo="Femenino",
        grupo_sanguineo="B+",
        pais_nacimiento="Colombia",
        departamento_nacimiento="Valle del Cauca",
        ciudad_nacimiento="Cali",
        zona_residencia="U"
    )
    
    # Familia y Acudientes
    FamiliaAcudientes.objects.create(
        paciente=paciente,
        acudiente_nombre="Diana Carolina Gómez Ruiz",
        acudiente_parentesco="Hija",
        acudiente_telefono="6023456789",
        acudiente_celular="3157654321",
        acudiente_direccion="Avenida 6N # 25-18, Cali",
        acudiente_email="diana.gomez@email.com",
        acudiente_estado_civil="S"
    )
    
    # Grado de Escolaridad
    GradoEscolaridad.objects.create(
        paciente=paciente,
        lee="1",
        escribe="1",
        primaria_completa="1",
        secundaria_completa="1",
        tecnico="",
        tecnologo="",
        profesional="Contadora Pública",
        maestria="Especialización en Finanzas",
        otros_estudios=""
    )
    
    # Datos Socioeconómicos
    DatosSocioEconomicosForm.objects.create(
        paciente=paciente,
        actividad_desempenada="Contadora independiente",
        ocupacion_actual="Consultora contable medio tiempo",
        aporte_familiar="0",
        jubilacion="1",
        renta_propia="1",
        otros_ingresos="Consultoría contable ocasional"
    )
    
    # Tipo de Familia
    TipoFamilia.objects.create(
        paciente=paciente,
        tipo_familia="FMC",  # Familia Monoparental Compuesta
        otro_razon_tipo_familia=""
    )
    
    # Seguridad Social
    SeguridadSocialSalud.objects.create(
        paciente=paciente,
        regimen_seguridad_social="CONTRIBUTIVO",
        afiliacion_salud="Sanitas",
        ips="Centro Médico Imbanaco"
    )
    
    # Relaciones Intrafamiliares
    RelacionesIntrafamiliares.objects.create(
        paciente=paciente,
        tipo_relacion="BUENA",
        maltrato="0",
        explicacion_relacion="Mantiene buena relación con sus dos hijas. Se reúnen semanalmente.",
        tipo_maltrato=""
    )
    
    # Protección Exequial
    ProteccionExequial.objects.create(
        paciente=paciente,
        proteccion_exequial="1",
        compania_proteccion_exequial="Los Olivos"
    )
    
    # Espiritualidad
    EspiritualidadReligion.objects.create(
        paciente=paciente,
        grupo_religioso="1",
        cual_grupo_religioso="Cristiana evangélica",
        religion="Evangélica",
        practica_religiosa="CULTO",
        otros_practicas_religiosas=""
    )
    
    # Hábitos y Rutinas
    HabitosRutinas.objects.create(
        paciente=paciente,
        actividad_fisica="1",
        tipo_actividad_fisica="Natación 2 veces por semana, baile",
        actividades_recreativas="Coro de la iglesia, clases de pintura, club de lectura"
    )
    
    # Aspectos Físicos
    AspectosFisicosSalud.objects.create(
        paciente=paciente,
        estado_salud="BUENA",
        explicacion_estado_salud="Buen estado físico general. Osteoartritis leve en rodillas."
    )
    
    # Medicamentos
    Medicamentos.objects.create(
        paciente=paciente,
        nombre_medicamento="Calcio + Vitamina D",
        dosis="600mg cada 24 horas",
        observaciones="Prevención osteoporosis"
    )
    
    Medicamentos.objects.create(
        paciente=paciente,
        nombre_medicamento="Glucosamina",
        dosis="1500mg cada 24 horas",
        observaciones="Salud articular"
    )
    
    # Adversidades a Medicamentos
    AdversidadesMedicamentos.objects.create(
        paciente=paciente,
        reacciones_adversas="0",
        descripcion_reacciones="",
        alergias_medicamentos="1",
        descripcion_alergias="Alergia a penicilina (rash cutáneo)",
        autprescripcion_medicamentos="0"
    )
    
    # Adversidades a Alimentos
    AdversidadesAlimentos.objects.create(
        paciente=paciente,
        adversidad_alimentos="1",
        descripcion_adversidad="Intolerancia a lactosa",
        alergias_alimentos="0",
        descripcion_alergias_alimentos=""
    )
    
    # Antecedentes Tóxicos
    AntecedentesToxicos.objects.create(
        paciente=paciente,
        consumo_sustancias="1",
        consumo_sustancias_tabaco="0",
        consumo_sustancias_cafe="1",
        consumo_sustancias_psicoactivas="0",
        frecuencia_consumo="Ocasional",
        cantidad_consumo="1 taza"
    )
    
    print(f"✅ Paciente creado: {paciente}")
    return paciente


def crear_paciente_4():
    """
    Paciente 4: Roberto Carlos Pérez Díaz
    Hombre de 76 años, viudo, con problemas cardíacos
    """
    print("\n🔵 Creando Paciente 4: Roberto Carlos Pérez Díaz...")
    
    # Identificación
    paciente = Identificacion.objects.create(
        primer_nombre="Roberto Carlos",
        segundo_nombre="",
        primer_apellido="Pérez",
        segundo_apellido="Díaz",
        fecha_nacimiento=date(1950, 5, 30),
        edad=76,
        tipo_documento="CC",
        numero_documento_paciente="19567890",
        ciudad_residencia="Barranquilla",
        sexo="Masculino",
        grupo_sanguineo="AB+",
        pais_nacimiento="Colombia",
        departamento_nacimiento="Atlántico",
        ciudad_nacimiento="Barranquilla",
        zona_residencia="U"
    )
    
    # Familia y Acudientes
    FamiliaAcudientes.objects.create(
        paciente=paciente,
        acudiente_nombre="Claudia Patricia Pérez Gómez",
        acudiente_parentesco="Hija",
        acudiente_telefono="6057890123",
        acudiente_celular="3006543210",
        acudiente_direccion="Calle 84 # 45-67, Barranquilla",
        acudiente_email="claudia.perez@email.com",
        acudiente_estado_civil="C"
    )
    
    # Grado de Escolaridad
    GradoEscolaridad.objects.create(
        paciente=paciente,
        lee="1",
        escribe="1",
        primaria_completa="1",
        secundaria_completa="1",
        tecnico="",
        tecnologo="",
        profesional="Ingeniero Civil",
        maestria="",
        otros_estudios="Cursos de actualización técnica"
    )
    
    # Datos Socioeconómicos
    DatosSocioEconomicosForm.objects.create(
        paciente=paciente,
        actividad_desempenada="Ingeniero de obras civiles",
        ocupacion_actual="Jubilado",
        aporte_familiar="1",
        jubilacion="1",
        renta_propia="0",
        otros_ingresos=""
    )
    
    # Tipo de Familia
    TipoFamilia.objects.create(
        paciente=paciente,
        tipo_familia="FE",  # Familia Extensa
        otro_razon_tipo_familia=""
    )
    
    # Seguridad Social
    SeguridadSocialSalud.objects.create(
        paciente=paciente,
        regimen_seguridad_social="CONTRIBUTIVO",
        afiliacion_salud="Salud Total",
        ips="Clínica la Asunción"
    )
    
    # Relaciones Intrafamiliares
    RelacionesIntrafamiliares.objects.create(
        paciente=paciente,
        tipo_relacion="REGULAR",
        maltrato="0",
        explicacion_relacion="Relación distante con algunos familiares. Vive solo pero recibe visitas de su hija.",
        tipo_maltrato=""
    )
    
    # Protección Exequial
    ProteccionExequial.objects.create(
        paciente=paciente,
        proteccion_exequial="1",
        compania_proteccion_exequial="Jardines del Recuerdo"
    )
    
    # Espiritualidad
    EspiritualidadReligion.objects.create(
        paciente=paciente,
        grupo_religioso="1",
        cual_grupo_religioso="Católico",
        religion="Católica",
        practica_religiosa="LECTURA",
        otros_practicas_religiosas=""
    )
    
    # Hábitos y Rutinas
    HabitosRutinas.objects.create(
        paciente=paciente,
        actividad_fisica="0",
        tipo_actividad_fisica="",
        actividades_recreativas="Televisión, lectura de periódicos"
    )
    
    # Aspectos Físicos
    AspectosFisicosSalud.objects.create(
        paciente=paciente,
        estado_salud="REGULAR",
        explicacion_estado_salud="Insuficiencia cardíaca controlada. Hipertensión arterial. Limitación en actividades físicas."
    )
    
    # Medicamentos
    Medicamentos.objects.create(
        paciente=paciente,
        nombre_medicamento="Carvedilol",
        dosis="25mg cada 12 horas",
        observaciones="Insuficiencia cardíaca"
    )
    
    Medicamentos.objects.create(
        paciente=paciente,
        nombre_medicamento="Furosemida",
        dosis="40mg cada 24 horas",
        observaciones="Diurético"
    )
    
    Medicamentos.objects.create(
        paciente=paciente,
        nombre_medicamento="Losartán",
        dosis="100mg cada 24 horas",
        observaciones="Hipertensión arterial"
    )
    
    Medicamentos.objects.create(
        paciente=paciente,
        nombre_medicamento="Espironolactona",
        dosis="25mg cada 24 horas",
        observaciones="Insuficiencia cardíaca"
    )
    
    # Adversidades a Medicamentos
    AdversidadesMedicamentos.objects.create(
        paciente=paciente,
        reacciones_adversas="1",
        descripcion_reacciones="Mareos ocasionales, posiblemente por Furosemida",
        alergias_medicamentos="0",
        descripcion_alergias="",
        autprescripcion_medicamentos="0"
    )
    
    # Adversidades a Alimentos
    AdversidadesAlimentos.objects.create(
        paciente=paciente,
        adversidad_alimentos="0",
        descripcion_adversidad="",
        alergias_alimentos="0",
        descripcion_alergias_alimentos=""
    )
    
    # Antecedentes Tóxicos
    AntecedentesToxicos.objects.create(
        paciente=paciente,
        consumo_sustancias="1",
        consumo_sustancias_tabaco="0",
        consumo_sustancias_cafe="0",
        consumo_sustancias_psicoactivas="0",
        frecuencia_consumo="Ex-fum.",
        cantidad_consumo="15 a sin"
    )
    
    print(f"✅ Paciente creado: {paciente}")
    return paciente


def crear_paciente_5():
    """
    Paciente 5: Gloria Inés Vargas Sánchez
    Mujer de 69 años, casada, zona rural, salud regular
    """
    print("\n🔵 Creando Paciente 5: Gloria Inés Vargas Sánchez...")
    
    # Identificación
    paciente = Identificacion.objects.create(
        primer_nombre="Gloria Inés",
        segundo_nombre="",
        primer_apellido="Vargas",
        segundo_apellido="Sánchez",
        fecha_nacimiento=date(1957, 9, 12),
        edad=69,
        tipo_documento="CC",
        numero_documento_paciente="51678901",
        ciudad_residencia="Manizales",
        sexo="Femenino",
        grupo_sanguineo="O-",
        pais_nacimiento="Colombia",
        departamento_nacimiento="Caldas",
        ciudad_nacimiento="Manizales",
        zona_residencia="R"  # Rural
    )
    
    # Familia y Acudientes
    FamiliaAcudientes.objects.create(
        paciente=paciente,
        acudiente_nombre="Pedro Antonio Vargas López",
        acudiente_parentesco="Esposo",
        acudiente_telefono="6068901234",
        acudiente_celular="3123456789",
        acudiente_direccion="Vereda La Esperanza, Km 12 vía Manizales",
        acudiente_email="pedro.vargas@email.com",
        acudiente_estado_civil="C"
    )
    
    # Grado de Escolaridad
    GradoEscolaridad.objects.create(
        paciente=paciente,
        lee="1",
        escribe="1",
        primaria_completa="1",
        secundaria_completa="0",
        tecnico="",
        tecnologo="",
        profesional="",
        maestria="",
        otros_estudios="Cursos de agricultura sostenible"
    )
    
    # Datos Socioeconómicos
    DatosSocioEconomicosForm.objects.create(
        paciente=paciente,
        actividad_desempenada="Agricultura y ventas",
        ocupacion_actual="Agricultora - finca familiar",
        aporte_familiar="1",
        jubilacion="0",
        renta_propia="1",
        otros_ingresos="Venta de productos agrícolas"
    )
    
    # Tipo de Familia
    TipoFamilia.objects.create(
        paciente=paciente,
        tipo_familia="FN",  # Familia Nuclear
        otro_razon_tipo_familia=""
    )
    
    # Seguridad Social
    SeguridadSocialSalud.objects.create(
        paciente=paciente,
        regimen_seguridad_social="SUBSIDIADO",
        afiliacion_salud="Asmet Salud",
        ips="Hospital Santa Sofía"
    )
    
    # Relaciones Intrafamiliares
    RelacionesIntrafamiliares.objects.create(
        paciente=paciente,
        tipo_relacion="BUENA",
        maltrato="0",
        explicacion_relacion="Convive con su esposo. Buena relación familiar. Sus hijos viven en la ciudad.",
        tipo_maltrato=""
    )
    
    # Protección Exequial
    ProteccionExequial.objects.create(
        paciente=paciente,
        proteccion_exequial="0",
        compania_proteccion_exequial=""
    )
    
    # Espiritualidad
    EspiritualidadReligion.objects.create(
        paciente=paciente,
        grupo_religioso="1",
        cual_grupo_religioso="Católica",
        religion="Católica",
        practica_religiosa="ORACION",
        otros_practicas_religiosas="Novenas en casa"
    )
    
    # Hábitos y Rutinas
    HabitosRutinas.objects.create(
        paciente=paciente,
        actividad_fisica="1",
        tipo_actividad_fisica="Trabajo en la finca - actividades agrícolas",
        actividades_recreativas="Jardinería, radio, visitas familiares"
    )
    
    # Aspectos Físicos
    AspectosFisicosSalud.objects.create(
        paciente=paciente,
        estado_salud="REGULAR",
        explicacion_estado_salud="Dolor crónico en articulaciones por trabajo físico. Varices en piernas."
    )
    
    # Medicamentos
    Medicamentos.objects.create(
        paciente=paciente,
        nombre_medicamento="Acetaminofén",
        dosis="500mg cada 8 horas si hay dolor",
        observaciones="Dolor articular"
    )
    
    Medicamentos.objects.create(
        paciente=paciente,
        nombre_medicamento="Diclofenaco gel",
        dosis="Aplicación tópica 3 veces al día",
        observaciones="Dolor en rodillas"
    )
    
    # Adversidades a Medicamentos
    AdversidadesMedicamentos.objects.create(
        paciente=paciente,
        reacciones_adversas="0",
        descripcion_reacciones="",
        alergias_medicamentos="0",
        descripcion_alergias="",
        autprescripcion_medicamentos="1"
    )
    
    # Adversidades a Alimentos
    AdversidadesAlimentos.objects.create(
        paciente=paciente,
        adversidad_alimentos="0",
        descripcion_adversidad="",
        alergias_alimentos="0",
        descripcion_alergias_alimentos=""
    )
    
    # Antecedentes Tóxicos
    AntecedentesToxicos.objects.create(
        paciente=paciente,
        consumo_sustancias="1",
        consumo_sustancias_tabaco="0",
        consumo_sustancias_cafe="1",
        consumo_sustancias_psicoactivas="0",
        frecuencia_consumo="3/día",
        cantidad_consumo="3 tazas"
    )
    
    print(f"✅ Paciente creado: {paciente}")
    return paciente


def main():
    """Función principal que ejecuta la creación de todos los Usuarios"""
    print("\n" + "="*70)
    print("🏥 GENERACIÓN DE 5 Usuarios CON INFORMACIÓN DIVERSA")
    print("Sistema Gerontología App")
    print("="*70)
    
    try:
        paciente1 = crear_paciente_1()
        paciente2 = crear_paciente_2()
        paciente3 = crear_paciente_3()
        paciente4 = crear_paciente_4()
        paciente5 = crear_paciente_5()
        
        print("\n" + "="*70)
        print("✅ TODOS LOS Usuarios CREADOS EXITOSAMENTE")
        print("="*70)
        print("\n📊 RESUMEN DE Usuarios CREADOS:")
        print(f"1. {paciente1}")
        print(f"2. {paciente2}")
        print(f"3. {paciente3}")
        print(f"4. {paciente4}")
        print(f"5. {paciente5}")
        print("\n" + "="*70)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
