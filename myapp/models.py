# ======================================================
# 🧠 MODELOS BASE DEL SISTEMA GERONTOLÓGICO
# ======================================================
# Autor: Manuel Maldonado
# Proyecto: Gerontología App
# Django 5.2.7
# ======================================================

from django.db import models
from django.conf import settings


# ======================================================
# 🌎 MODELOS GEOGRÁFICOS
# ======================================================

class Pais(models.Model):
    """Representa un país registrado en el sistema."""
    nombre_pais = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_pais


class Departamento(models.Model):
    """Representa un departamento o estado, vinculado a un país."""
    nombre_departamento = models.CharField(max_length=255)
    fk_pais = models.ForeignKey(Pais, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre_departamento} ({self.fk_pais})"


class Ciudad(models.Model):
    """Representa una ciudad, vinculada a un departamento."""
    nombre_ciudad = models.CharField(max_length=100)
    fk_departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre_ciudad} - {self.fk_departamento}"


# ======================================================
# 📄 TIPOS DE DOCUMENTOS
# ======================================================

class TipoDocumento(models.Model):
    """Define los diferentes tipos de documentos de identidad."""
    TIPO_DOCUMENTO_CHOICES = [
        ('RC', 'Registro Civil'),
        ('TI', 'Tarjeta de Identidad'),
        ('TE', 'Tarjeta de Extranjería'),
        ('CE', 'Cédula de Extranjería'),
        ('NIT', 'Número de Identificación Tributaria'),
        ('PP', 'Pasaporte'),
        ('PEP', 'Permiso Especial de Permanencia'),
        ('DIE', 'Documento de Identificación Extranjero'),
        ('NUIP', 'NUIP'),
        ('FOREIGN_NIT', 'NIT de otro país'),
    ]

    tipo_documento = models.CharField(max_length=11, choices=TIPO_DOCUMENTO_CHOICES)

    def __str__(self):
        return self.get_tipo_documento_display()


# ======================================================
# 💰 DATOS SOCIOECONÓMICOS
# ======================================================

class DatosSocioeconomico(models.Model):
    """Registra información económica del usuario."""
    actividad_desempeñada = models.CharField(max_length=255)
    actividad_actual = models.CharField(max_length=255)
    tipo_ingreso = models.CharField(max_length=255)
    valor_mensual_promedio = models.FloatField()
    clasificacion_ingreso = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.actividad_actual} - ${self.valor_mensual_promedio:,.2f}"


# ======================================================
# 👤 DATOS DEL USUARIO
# ======================================================

class Usuario(models.Model):
    """Modelo principal que almacena información personal, de contacto y relaciones del usuario."""

    # 📛 DATOS PERSONALES
    segundo_apellido = models.CharField(max_length=100, blank=True)
    celular = models.CharField(max_length=30, blank=True)
    tel_fijo = models.CharField(max_length=30, default='N/A')
    direccion = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    grupo_sanguineo = models.CharField(max_length=3)
    genero = models.CharField(max_length=50)
    matricula_profesional = models.CharField(max_length=255, default='N/A')
    numero_documento = models.CharField(max_length=50)

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    ESTADO_CIVIL_CHOICES = [
        ('S', 'Soltero'),
        ('C', 'Casado'),
        ('V', 'Viudo'),
        ('D', 'Divorciado'),
        ('UL', 'Unión Libre'),
    ]
    estado_civil = models.CharField(max_length=11, choices=ESTADO_CIVIL_CHOICES)

    PROCEDENCIA_CHOICES = [
        ('U', 'Urbano'),
        ('R', 'Rural'),
    ]
    lugar_tipo_procedencia = models.CharField(max_length=1, choices=PROCEDENCIA_CHOICES)

    # 🔗 RELACIONES
    fk_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fk_datos_socioeconomicos = models.OneToOneField(DatosSocioeconomico, on_delete=models.CASCADE)
    fk_tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.numero_documento})"
