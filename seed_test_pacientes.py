"""
Script simple para crear pacientes de prueba en la BD local (SQLite)
Ejecutar: venv\Scripts\python.exe seed_test_pacientes.py
"""
import os
import sys
import django
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings_local'
django.setup()

from myapp.models import Identificacion

pacientes_data = [
    {
        "primer_nombre": "María Elena",    "segundo_nombre": "",
        "primer_apellido": "Rodríguez",   "segundo_apellido": "García",
        "numero_documento_paciente": "41234567", "tipo_documento": "CC",
        "edad": 78, "sexo": "Femenino",
        "ciudad_residencia": "Bogotá",    "zona_residencia": "U",
        "grupo_sanguineo": "O+",
        "pais_nacimiento": "Colombia",    "departamento_nacimiento": "Cundinamarca",
        "ciudad_nacimiento": "Bogotá",
    },
    {
        "primer_nombre": "José Alberto",   "segundo_nombre": "",
        "primer_apellido": "Martínez",    "segundo_apellido": "López",
        "numero_documento_paciente": "17345678", "tipo_documento": "CC",
        "edad": 82, "sexo": "Masculino",
        "ciudad_residencia": "Medellín",  "zona_residencia": "U",
        "grupo_sanguineo": "A+",
        "pais_nacimiento": "Colombia",    "departamento_nacimiento": "Antioquia",
        "ciudad_nacimiento": "Medellín",
    },
    {
        "primer_nombre": "Carmen Rosa",    "segundo_nombre": "",
        "primer_apellido": "Vargas",      "segundo_apellido": "Herrera",
        "numero_documento_paciente": "51456789", "tipo_documento": "CC",
        "edad": 75, "sexo": "Femenino",
        "ciudad_residencia": "Cali",      "zona_residencia": "U",
        "grupo_sanguineo": "B+",
        "pais_nacimiento": "Colombia",    "departamento_nacimiento": "Valle del Cauca",
        "ciudad_nacimiento": "Cali",
    },
    {
        "primer_nombre": "Luis Fernando",  "segundo_nombre": "",
        "primer_apellido": "González",    "segundo_apellido": "Pérez",
        "numero_documento_paciente": "19567890", "tipo_documento": "CC",
        "edad": 80, "sexo": "Masculino",
        "ciudad_residencia": "Barranquilla", "zona_residencia": "U",
        "grupo_sanguineo": "O-",
        "pais_nacimiento": "Colombia",    "departamento_nacimiento": "Atlántico",
        "ciudad_nacimiento": "Barranquilla",
    },
    {
        "primer_nombre": "Ana Lucía",      "segundo_nombre": "",
        "primer_apellido": "Torres",      "segundo_apellido": "Moreno",
        "numero_documento_paciente": "51678901", "tipo_documento": "CC",
        "edad": 71, "sexo": "Femenino",
        "ciudad_residencia": "Bucaramanga", "zona_residencia": "U",
        "grupo_sanguineo": "AB+",
        "pais_nacimiento": "Colombia",    "departamento_nacimiento": "Santander",
        "ciudad_nacimiento": "Bucaramanga",
    },
]

print("=" * 60)
print("SEMBRANDO PACIENTES DE PRUEBA EN SQLite")
print("=" * 60)

creados = 0
omitidos = 0

for data in pacientes_data:
    doc = data["numero_documento_paciente"]
    if Identificacion.objects.filter(numero_documento_paciente=doc).exists():
        print(f"⚠️  Ya existe: {data['primer_nombre']} {data['primer_apellido']} ({doc})")
        omitidos += 1
    else:
        Identificacion.objects.create(**data)
        print(f"✅ Creado:    {data['primer_nombre']} {data['primer_apellido']} ({doc})")
        creados += 1

print()
print(f"Resultado: {creados} creados, {omitidos} ya existían")
print()
print("Documentos para probar en la búsqueda:")
for p in Identificacion.objects.all():
    print(f"  {p.numero_documento_paciente}  →  {p.primer_nombre} {p.primer_apellido}")
print("=" * 60)
