# ======================================================
# 🧠 MODELOS BASE DEL SISTEMA GERONTOLÓGICO
# ======================================================
# Autor: Manuel Maldonado
# Proyecto: Gerontología App
# Django 5.2.7
# ======================================================

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator



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

# ======================================================
# Clases para Historia Gerontológica
# ======================================================
# Autor: Daniel Bernal
# Proyecto: Gerontología App
# Django 5.2.7
# ======================================================

class Identificacion(models.Model):
    
    # Datos Personales del Paciente
    
    # paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100, blank=True)
    primer_apellido = models.CharField(max_length=100)    
    segundo_apellido = models.CharField(max_length=100, blank=True)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    tipo_documento = models.CharField(max_length=11)
    numero_documento_paciente = models.CharField(max_length=50)
    ciudad_residencia = models.CharField(max_length=255)
    sexo = models.CharField(max_length=50) # genero
    grupo_sanguineo = models.CharField(max_length=3)
    pais_nacimiento = models.CharField(max_length=255)
    departamento_nacimiento = models.CharField(max_length=255)
    ciudad_nacimiento = models.CharField(max_length=255)
    
    ZONA_RESIDENCIA_CHOICES = [
        ('U', 'Urbano'),                
        ('R', 'Rural'),
    ]
    
    zona_residencia = models.CharField(max_length=1, choices=ZONA_RESIDENCIA_CHOICES, default='U')  # Urbano/Rural
    
    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido} - {self.numero_documento_paciente}"
    
class FamiliaAcudientes(models.Model):
    
    # Datos del Acudiente o Familiar Responsable
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    acudiente_nombre = models.CharField(max_length=255)
    acudiente_parentesco = models.CharField(max_length=100)
    acudiente_telefono = models.CharField(max_length=30, blank=True)
    acudiente_celular = models.CharField(max_length=30)
    acudiente_direccion = models.CharField(max_length=255)
    acudiente_email = models.CharField(max_length=255)
    
    ESTADO_CIVIL_CHOICES = [
        ('S', 'Soltero(a)'),
        ('C', 'Casado(a)'),
        ('UL', 'Unión Libre'),
        ('D', 'Divorciado(a)'),
        ('V', 'Viudo(a)'),
        ('SE', 'Separado(a)'),
    ]
    
    acudiente_estado_civil = models.CharField(max_length=2, choices=ESTADO_CIVIL_CHOICES)
    
    def __str__(self):
        return f"{self.acudiente_nombre} - {self.acudiente_parentesco}"
    
class GradoEscolaridad(models.Model):
    
    # Datos Escolares del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    SI_NO_CHOICES = [
        ('1', 'Si'),
        ('0', 'No'),
    ]
    
    #habilidades basicas
    lee = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='1')
    escribe = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='1')
    
    #Educacion formal
    primaria_completa = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='1')
    secundaria_completa = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='1')
    
    #Educacion tecnica y superior
    tecnico = models.CharField(max_length=255, blank=True)
    tecnologo = models.CharField(max_length=255, blank=True)
    profesional = models.CharField(max_length=255, blank=True)
    maestria = models.CharField(max_length=255, blank=True)
    otros_estudios = models.CharField(max_length=500, blank=True)
    
    def __str__(self):
        return f"Escolaridad: Primaria({self.primaria_completa}), Secundaria({self.secundaria_completa})"
    
class DatosSocioEconomicosForm(models.Model):   
    
    # Datos Socio Economicos del Paciente
     
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    # Actividad laboral desempeñada
    
    actividad_desempeñada = models.CharField(max_length=255)
    ocupacion_actual = models.CharField(max_length=255)
    
    # Origen de los ingresos actuales
    
    SI_NO_CHOICES = [    
        ('1', 'Si'),
        ('0', 'No'),    
    ]
    
    aporte_familiar = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='1')
    jubilacion = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='1')
    renta_propia = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='1')
    otros_ingresos = models.CharField(max_length=500, blank=True)
    
    def __str__(self):
        return f"Datos Socio Económicos de: {self.paciente}"
    
class TipoFamilia(models.Model):
    
    # Tipo de Familia del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    TIPO_FAMILIA_CHOICES = [
        ('FN', 'Familia Nuclear'),
        ('FE', 'Familia Extensa'),
        ('FA', 'Familia Ampliada'),
        ('FME', 'Familia Multiespecie'),
        ('FC', 'Familia Compuesta'),
        ('FMR', 'Familia Mixta o Reconstituida'),
        ('FMS', 'Familia Monoparental Simple'),
        ('FMC', 'Familia Monoparental Compuesta'),
        ('FH', 'Familia Homoparental'),
        ('O', 'Otro tipo de convivencia'),
    ]
    
    otro_razon_tipo_familia = models.TextField(blank=True)

    tipo_familia = models.CharField(max_length=11, choices=TIPO_FAMILIA_CHOICES)
    
    def __str__(self):
        return f"{self.get_tipo_familia_display()}"
    
class SeguridadSocialSalud(models.Model):
    
    # Informacion de afiliacion, EPS e IPS del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    REGIMEN_SEGURIDAD_SOCIAL_CHOICES = [
        ('CONTRIBUTIVO', 'Contributivo'),
        ('SUBSIDIADO', 'Subsidiado'),
        ('ESPECIALES', 'Especiales'),
        ('SIN_SEGURIDAD', 'Sin seguridad'),
    ]
    
    regimen_seguridad_social = models.CharField(max_length=255, choices=REGIMEN_SEGURIDAD_SOCIAL_CHOICES)
    afiliacion_salud = models.CharField(max_length=255)
    ips = models.CharField(max_length=255)
    
    def __str__(self):
        return f"Regimen: {self.regimen_seguridad_social}, Afiliacion: {self.afiliacion_salud}, IPS: {self.ips}"
    
class RelacionesIntrafamiliares(models.Model):
    
    # Relaciones Intrafamiliares del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    TIPO_RELACION_CHOICES = [
        ('BUENA', 'Buena'),
        ('REGULAR', 'Regular'),        
        ('MALA', 'Mala'),
    ]
    
    tipo_relacion = models.CharField(max_length=11, choices=TIPO_RELACION_CHOICES)
    
    SI_NO_CHOICES = [    
        ('1', 'Si'),
        ('0', 'No'),    
    ]
    
    maltrato = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    
    explicacion_relacion = models.TextField(blank=True)
    tipo_maltrato = models.CharField(max_length=255, blank=True)
    
    def __str__(self):  
        return f"Relación Intrafamiliar: {self.get_tipo_relacion_display()}"
    
class ProteccionExequial(models.Model):
    
     # Proteccion Exequial del Paciente
     
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    SI_NO_CHOICES = [    
        ('1', 'Si'),
        ('0', 'No'),    
    ]
     
    proteccion_exequial = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')    
    compania_proteccion_exequial = models.TextField(blank=True)
    
    def __str__(self):
        return f"Protección Exequial: {'Sí' if self.proteccion_exequial else 'No'}"
    
class EspiritualidadReligion(models.Model):
    
    # Espiritualidad y Religion del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    SI_NO_CHOICES = [    
        ('1', 'Si'),
        ('0', 'No'),    
    ]
    
    grupo_religioso = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='1')
    cual_grupo_religioso = models.CharField(max_length=255, blank=True)
    religion = models.CharField(max_length=255, blank=True)
    
    PRACTICA_RELIGIOSA_CHOICES = [
        ('MISA', 'Misa'),
        ('CULTO', 'Culto'),
        ('LECTURA', 'Lectura de textos sagrados'),
        ('ORACION','Grupos de oración'),
        ('OTROS', 'Otros'),        
    ]
    
    practica_religiosa = models.CharField(max_length=11, choices=PRACTICA_RELIGIOSA_CHOICES)
    otros_practicas_religiosas = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f"Religión: {self.religion}, Práctica: {self.get_practica_religiosa_display()}" 
    
class HabitosRutinas(models.Model):
    
    # Habitos y Rutinas del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    SI_NO_CHOICES = [    
        ('1', 'Si'),
        ('0', 'No'),    
    ]
        
    actividad_fisica = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    tipo_actividad_fisica = models.CharField(max_length=255, blank=True)
    actividades_recreativas = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f"Hábitos y Rutinas de: {self.paciente}"
    
class AspectosFisicosSalud(models.Model):
    
    # Aspectos Fisicos y Salud del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    ESTADO_SALUD_CHOICES = [ 
        ('BUENA', 'Buena'), 
        ('REGULAR', 'Regular'), 
        ('MALA', 'Mala'), 
    ]
    
    estado_salud = models.CharField(max_length=11, choices=ESTADO_SALUD_CHOICES, default='BUENA')
    explicacion_estado_salud = models.TextField(blank=True)
    
    def __str__(self):
        return f"Aspectos Físicos y Salud de: {self.paciente}"
    
class Medicamentos(models.Model):
    
    # Medicamentos y dosis del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    nombre_medicamento = models.CharField(max_length=255)
    dosis = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre_medicamento} - {self.dosis} - {self.observaciones}"

class AdversidadesMedicamentos(models.Model):
    
    # Reacciones Adversas a Medicamentos del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    SI_NO_CHOICES = [    
        ('1', 'Si'),
        ('0', 'No'),    
    ]
    
    reacciones_adversas = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    descripcion_reacciones = models.TextField(blank=True)
    alergias_medicamentos = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    descripcion_alergias = models.TextField(blank=True)
    autprescripcion_medicamentos = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    
    def __str__(self):
        return f"Adversidades a Medicamentos: {'Sí' if self.reacciones_adversas else 'No'}"
    
class AdversidadesAlimentos(models.Model):
    
    # Reacciones Adversas a Alimentos del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    SI_NO_CHOICES = [    
        ('1', 'Si'),
        ('0', 'No'),    
    ]
    
    adversidad_alimentos = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    descripcion_adversidad = models.TextField(blank=True)
    alergias_alimentos = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    descripcion_alergias_alimentos = models.TextField(blank=True)
    
    def __str__(self):
        return f"Adversidades a Alimentos: {'Sí' if self.adversidad_alimentos else 'No'}"
    
class AntecedentesToxicos(models.Model):
    
    # Antecedentes Toxicos del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    SI_NO_CHOICES = [    
        ('1', 'Si'),
        ('0', 'No'),    
    ]
    
    FRECUENCIA_CONSUMO_CHOICES = [
        ('DIARIO', 'Diario'),
        ('SEMANAL', 'Semanal'),
    ]
    
    consumo_sustancias = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0') # Alcohol
    consumo_sustancias_tabaco = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0') # Tabaco
    consumo_sustancias_cafe = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0') # Cafe
    consumo_sustancias_psicoactivas = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0') # Psicoactivas
    frecuencia_consumo = models.CharField(max_length=10, choices=FRECUENCIA_CONSUMO_CHOICES) # Frecuencia diario/semanal
    cantidad_consumo = models.CharField(max_length=100) # Cantidad consumida segun la frecuencia/sustancia seleccionada
    
    def __str__(self):
        return f"Antecedentes Tóxicos: {'Sí' if self.consumo_sustancias and self.cantidad_consumo else 'No'}"
    
class RevisionPorSistemas(models.Model):
    
    # Revisión por Sistemas del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    SI_NO_CHOICES = [    
        ('1', 'Si'),
        ('0', 'No'),    
    ]

    # a. Órganos de los sentidos
    cataratas = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    ceguera = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    presbiacusia = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    glaucoma = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    sentidos_otros = models.CharField(max_length=255, blank=True, null=True)

    # b. Sistema cardiovascular
    infarto_miocardio = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    hta = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    insuficiencia_cardiaca = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    arteriosclerosis = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    cardiovascular_otros = models.CharField(max_length=255, blank=True, null=True)

    # c. Sistema respiratorio
    epoc = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    bronquitis = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    asma = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    neumonia = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    respiratorio_otros = models.CharField(max_length=255, blank=True, null=True)

    # d. Sistema óseo muscular
    artritis = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    osteoporosis = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    osteoartrosis = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    lumbago = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    oseo_muscular_otros = models.CharField(max_length=255, blank=True, null=True)

    # e. Sistema urinario
    anuria = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    cistitis = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    prostatitis = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    prolapso_genital = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    incontinencia_urinaria = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    urinario_otros = models.CharField(max_length=255, blank=True, null=True)

    # f. Sistema nervioso
    demencia_senil = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    alzheimer = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    parkinson = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    esquizofrenia = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    epilepsia = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    nervioso_otros = models.CharField(max_length=255, blank=True, null=True)

    # g. Sistema endocrino
    diabetes_mellitus = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    hipertiroidismo = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    hipotiroidismo = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    bocio = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    endocrino_otros = models.CharField(max_length=255, blank=True, null=True)

    # h. Sistema tegumentario
    prurito = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    urticaria = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    verrugas = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    quemaduras = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    tegumentario_otros = models.CharField(max_length=255, blank=True, null=True)

    # i. Sistema digestivo
    gastritis = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    diarrea = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    estrenimiento = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    ulcera_duodenal = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    digestivo_otros = models.CharField(max_length=255, blank=True, null=True)

    # j. Tumores
    tejido_mamario = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    sistema_digestivo = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    sistema_urinario = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    tumores_otros = models.CharField(max_length=255, blank=True, null=True)

    # Observaciones generales
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Revisión por Sistemas: {self.paciente}"
    
class EvaluacionBucal(models.Model):
    
    # Evaluación Bucal del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    SI_NO_CHOICES = [    
        ('1', 'Si'),
        ('0', 'No'),    
    ]
    
    piezas_dentales_completas = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')    
    piezas_dentales_incompletas = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    protesis = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    observasiones = models.TextField(blank=True)
    
    def __str__(self):    
        return f"Evaluación Bucal: {self.paciente}"
    
class SindromesProblemasGriatricos(models.Model):
    
     # Sindromes y Problemas Geriátricos del Paciente
     
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    SI_NO_CHOICES = [    
        ('1', 'Si'),
        ('0', 'No'),    
    ]
    
    vertigo_mareo = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    delirio = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    caidas = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    numero_caidas = models.IntegerField()
    sincopes = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    dolor_cronico = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    deprivacion_auditiva = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    deprivacion_visual = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    insomnio = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    incontinencia_urinaria = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    otros_sindromes_problemas = models.TextField(blank=True)
    observaciones_generales = models.TextField(blank=True)
    observaciones_paciente = models.TextField(blank=True)
    
    def __str__(self):    
        return f"Sindromes y Problemas Geriatricos: {self.paciente}"
    
class ValoracionVidaDiariaKatz(models.Model):
    
    # Valoración de la Vida Diaria según Katz del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    alimentacion = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(6)])
    bano = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(6)])
    continencia = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(6)])
    movilidad = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(6)])
    uso_sanitarios = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(6)])
    vestido = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(6)])
    puntuacion_total = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(36)])
    observaciones = models.TextField(blank=True)
    
    def __str__(self):  
        return f"Valoración Vida Diaria Katz: {self.paciente}"
    
class AyudasOrtopedicas(models.Model):
    
    # Ayudas Ortopédicas del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    SI_NO_CHOICES = [    
        ('1', 'Si'),
        ('0', 'No'),    
    ]
    
    caminador = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    caminador_observaciones = models.TextField(blank=True)
    muletas = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    muletas_observaciones = models.TextField(blank=True)
    silla_de_ruedas = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    silla_de_ruedas_observaciones = models.TextField(blank=True)
    baston = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    baston_observaciones = models.TextField(blank=True)
    gafas = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    gafas_observaciones = models.TextField(blank=True)  
    audifonos = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    audifonos_observaciones = models.TextField(blank=True)
    protesis = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    protesis_observaciones = models.TextField(blank=True)
    otros = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    otros_observaciones = models.TextField(blank=True)
    
    def __str__(self):
        return f"Ayudas Ortopédicas: {self.paciente}"
    
class AspectosMentales(models.Model):
    
    # Aspectos Mentales del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    SI_NO_CHOICES = [    
        ('1', 'Si'),
        ('0', 'No'),    
    ]
    
    psicosis = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    ansiedad =models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    problemas_intergeneracionales = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    duelo = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    afectivo_bipolar = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    depresion = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    
    def __str__(self):
        return f"Aspectos Mentales: {self.paciente}"
    
class IdeasSuicidas(models.Model):
    
    # Ideas Suicidas del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    IDEAS_SUICIDAS_CHOICES = [                
        ('1', 'Sí'),        
        ('0', 'No'),
        ('2', 'A veces'),        
    ]
    
    ideas_suicidas = models.CharField(max_length=10, choices=IDEAS_SUICIDAS_CHOICES, default='0')
    explicacion_ideas_suicidas = models.TextField(blank=True)
    
    def __str__(self):
        return f"Ideas Suicidas: {self.paciente}"
    
class ValoracionMental(models.Model):
    
    # Valoración Mental del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    # Preguntas individuales
    fecha_hoy = models.CharField(max_length=50, blank=True)
    dia_semana = models.CharField(max_length=50, blank=True)
    lugar_actual = models.CharField(max_length=255, blank=True)
    numero_telefono = models.CharField(max_length=50, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    lugar_nacimiento = models.CharField(max_length=255, blank=True)
    presidente = models.CharField(max_length=100, blank=True)
    apellido_madre = models.CharField(max_length=100, blank=True)
    restar_tres_en_tres = models.CharField(max_length=100, blank=True)

    # Valoración cognitiva
    NIVEL_CHOICES = [
        ('NORMAL', 'Normal'),
        ('DC_LEVE', 'Deterioro Cognitivo Leve'),
        ('DC_MODERADO', 'Deterioro Cognitivo Moderado'),
        ('DC_SEVERO', 'Deterioro Cognitivo Severo'),
    ]
    nivel_cognitivo = models.CharField(max_length=20, choices=NIVEL_CHOICES, blank=True)
    errores_totales = models.IntegerField(null=True, blank=True)  # para calcular automáticamente el nivel

    observaciones = models.TextField(blank=True)
    
    def __str__(self):
        return f"Valoración Mental: {self.paciente}"
    
class EscalaYesavage(models.Model):
    
    # Valoración de Depresión según Escala de Yesavage del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    SI_NO_CHOICES = [    
        ('1', 'Si'),
        ('0', 'No'),    
    ]

    # Preguntas
    satisfecho_vida = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    satisfecho_vida_valor = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])

    renunciado_actividades = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    renunciado_actividades_valor = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])

    vida_vacia = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    vida_vacia_valor = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])

    aburrido = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    aburrido_valor = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])

    alegre_optimista = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    alegre_optimista_valor = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])

    temor_malo = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    temor_malo_valor = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])

    feliz = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    feliz_valor = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])

    desamparado = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    desamparado_valor = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])

    quedarse_casa = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    quedarse_casa_valor = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])

    fallos_memoria = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    fallos_memoria_valor = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])

    agradable_vivo = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    agradable_vivo_valor = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])

    duro_proyectos = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    duro_proyectos_valor = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])

    lleno_energia = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    lleno_energia_valor = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])

    situacion_angustiosa = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    situacion_angustiosa_valor = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])

    economicamente_mejor = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='0')
    economicamente_mejor_valor = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])
    
    def __str__(self):
        return f"Escala Yesavage: {self.paciente}"
    
class ValoracionGerontologicaGeneral(models.Model):
    
    # Valoración Gerontológica General del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    # Aspectos Sociales
    
    social_familiar_gerontologica = models.TextField()
    
    # Aspectos Físicos
    
    salud_fisica = models.TextField()
    enfermedades_en_tratamiento = models.TextField()
    medicamentos_actuales = models.TextField()
    
    # Aspectos Funcionales
    
    ACTIVIDADES_VIDA_DIARIA_CHOICES = [
        ('INDEPENDIENTE', 'Independiente'),
        ('DEPENDIENTE_PARCIAL', 'Dependiente Parcial'),
        ('DEPENDIENTE_TOTAL', 'Dependiente Total'),
    ]
    
    actividades_vida_diaria = models.CharField(max_length=20, choices=ACTIVIDADES_VIDA_DIARIA_CHOICES)
    
    # Aspectos Psicogerontológicos
    
    enfermedades_mentales = models.TextField()
    estado_salud_mental = models.TextField()
    
    DEPRESION_CHOICES = [
        ('NORMAL', 'Normal'),
        ('LEVE', 'Leve'),
        ('ESTABLECIDA', 'Establecida'),
    ]
    
    depresion = models.CharField(max_length=30, choices=DEPRESION_CHOICES)

    def __str__(self):
        return f"Valoración Gerontológica General: {self.paciente}"
    
class SeguimientoControlGerontologico(models.Model):
    
    # Seguimiento y Control Gerontológico del Paciente
    
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE)
    
    # Seguimiento y Control Gerontológico
    
    observaciones_seguimiento = models.TextField()
    fecha_seguimiento = models.DateField()
    
    nombre_profesional = models.CharField(max_length=255)
    firma_profesional = models.CharField(max_length=255)
    registro_profesional = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Seguimiento y Control Gerontológico: {self.paciente} - {self.fecha_seguimiento}"
    

class HistoriaGerontologica(models.Model):
    
    # Historia Gerontológica del Paciente
        
    # Identificación
    
    fk_identificacion = models.OneToOneField(Identificacion, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Familia o Acudientes
    
    fk_familia_acudientes = models.OneToOneField(FamiliaAcudientes, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Grado de Escolaridad
    
    fk_grado_escolaridad = models.OneToOneField(GradoEscolaridad, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Datos Socioeconómicos
    
    fk_datos_socio_economicos = models.OneToOneField(DatosSocioEconomicosForm, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Tipo de Familia
    
    fk_tipo_familia = models.OneToOneField(TipoFamilia, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Seguridad Social y Salud
    
    fk_seguridad_social_salud = models.OneToOneField(SeguridadSocialSalud, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Relaciones Intrafamiliares
    
    fk_relaciones_intrafamiliares = models.OneToOneField(RelacionesIntrafamiliares, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Proteccion Exequial
    
    fk_proteccion_exequial = models.OneToOneField(ProteccionExequial, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Espiritualidad y Religión
    
    fk_espiritualidad_religion = models.OneToOneField(EspiritualidadReligion, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Habitos y Rutinas
    
    fk_habitos_rutinas = models.OneToOneField(HabitosRutinas, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Aspectos Físicos y de Salud
    
    fk_aspectos_fisicos_salud = models.OneToOneField(AspectosFisicosSalud, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Medicamentos (Relación Many-to-Many)
    
    fk_medicamentos = models.ManyToManyField(Medicamentos, related_name='historia_gerontologica')
    
    # Adversidades a Medicamentos
    
    fk_adversidades_medicamentos = models.OneToOneField(AdversidadesMedicamentos, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Adversidades a Alimentos
    
    fk_adversidades_alimentos = models.OneToOneField(AdversidadesAlimentos, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Antecedentes Tóxicos
    
    fk_antecedentes_toxicos = models.OneToOneField(AntecedentesToxicos, on_delete=models.CASCADE, related_name='historia_gerontologica')   
    
    # Revisión por Sistemas
    
    fk_revision_por_sistemas = models.OneToOneField(RevisionPorSistemas, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Evaluación Bucal
    
    fk_evaluacion_bucal = models.OneToOneField(EvaluacionBucal, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Síndromes y Problemas Geriátricos
    
    fk_sindromes_problemas_griatricos = models.OneToOneField(SindromesProblemasGriatricos, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Valoración de la Vida Diaria según Katz
    
    fk_valoracion_vida_diaria_katz = models.OneToOneField(ValoracionVidaDiariaKatz, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Ayudas Ortopédicas
    
    fk_ayudas_ortopedicas = models.OneToOneField(AyudasOrtopedicas, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Aspectos Mentales
    
    fk_aspectos_mentales = models.OneToOneField(AspectosMentales, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Ideas Suicidas
    
    fk_ideas_suicidas = models.OneToOneField(IdeasSuicidas, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Valoración Mental
    
    fk_valoracion_mental = models.OneToOneField(ValoracionMental, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Escala de Yesavage
    
    fk_escala_yesavage = models.OneToOneField(EscalaYesavage, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Valoración Gerontológica General
    
    fk_valoracion_gerontologica_general = models.OneToOneField(ValoracionGerontologicaGeneral, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    # Seguimiento y Control Gerontológico
    
    fk_seguimiento_control_gerontologico = models.OneToOneField(SeguimientoControlGerontologico, on_delete=models.CASCADE, related_name='historia_gerontologica')
    
    def __str__(self):
        return f"Historia Gerontológica del Paciente: {self.fk_identificacion}"


# ======================================================
# MODELOS PARA MÓDULO DE ENFERMERÍA
# ======================================================

class EvolucionDiariaEnfermeria(models.Model):
    """Modelo para el registro diario de evolución de enfermería para personas mayores"""
    
    # Información del Paciente
    paciente = models.ForeignKey('Identificacion', on_delete=models.CASCADE, related_name='evoluciones_enfermeria')
    
    # Fecha del registro
    fecha = models.DateField()
    
    # Estado del día
    ESTADO_CHOICES = [
        ('B', 'Bueno'),
        ('R', 'Regular'),
        ('M', 'Malo'),
    ]
    
    paso_el_dia = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='B')
    
    # Alimentación
    alimentacion = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='B')
    
    # Eliminación (orina)
    elimina = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='B')
    
    # Exoneración (deposición)
    exonera = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='B')
    
    # Medicamentos
    SI_NO_CHOICES = [
        ('1', 'Sí'),
        ('0', 'No'),
    ]
    
    medicamentos = models.CharField(max_length=1, choices=SI_NO_CHOICES, default='1')
    
    # Signos Vitales
    frecuencia_cardiaca = models.CharField(max_length=10, blank=True, null=True, verbose_name='F.C.')
    presion_arterial = models.CharField(max_length=10, blank=True, null=True, verbose_name='P.A.')
    temperatura = models.CharField(max_length=10, blank=True, null=True, verbose_name='T')
    frecuencia_respiratoria = models.CharField(max_length=10, blank=True, null=True, verbose_name='F.R.')
    
    # Novedad
    novedad = models.CharField(max_length=1, choices=SI_NO_CHOICES, default='0')
    
    # Observaciones
    observacion = models.TextField(blank=True, null=True)
    
    # Información del profesional que registra
    nombre_profesional = models.CharField(max_length=255, verbose_name='Nombre de quien atiende')
    identificacion_profesional = models.CharField(max_length=50, verbose_name='Identificación')
    firma = models.CharField(max_length=255, blank=True, null=True)
    
    # Metadata
    fecha_registro = models.DateTimeField(auto_now_add=True)
    usuario_registro = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='evoluciones_registradas')
    
    class Meta:
        ordering = ['-fecha', '-fecha_registro']
        verbose_name = 'Evolución Diaria de Enfermería'
        verbose_name_plural = 'Evoluciones Diarias de Enfermería'
    
    def __str__(self):
        return f"Evolución {self.paciente.primer_nombre} {self.paciente.primer_apellido} - {self.fecha}"
    
# ======================================================
# MODELO PARA MÓDULO DEL MÉDICO
# ======================================================

from django.conf import settings  # si no está ya importado arriba, déjalo

class ConsultaMedica(models.Model):
    """
    Modelo para guardar una CONSULTA MÉDICA realizada por el médico
    a una persona mayor.
    """

    # Paciente al que se le hace la consulta (usa el modelo Identificacion)
    paciente = models.ForeignKey(
        Identificacion,
        on_delete=models.CASCADE,
        related_name='consultas_medicas'
    )

    # Fecha en la que se hace la consulta
    fecha = models.DateField()

    # Motivo de consulta (¿por qué vino el paciente?)
    motivo_consulta = models.TextField()

    # Diagnóstico médico (opcional al inicio)
    diagnostico = models.TextField(blank=True)

    # Plan de manejo (tratamiento, indicaciones, etc.)
    plan_manejo = models.TextField(blank=True)

    # Observaciones adicionales
    observaciones = models.TextField(blank=True)

    # Usuario que registra la consulta (Médico)
    medico = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='consultas_realizadas'
    )

    # Fecha y hora en que se guardó el registro
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha', '-fecha_registro']
        verbose_name = 'Consulta Médica'
        verbose_name_plural = 'Consultas Médicas'

    def __str__(self):
        return f"Consulta {self.paciente.primer_nombre} {self.paciente.primer_apellido} - {self.fecha}" 
    
# ======================================================
# ENUNCIADO - NOTAS GENERALES DEL MÉDICO
# ======================================================

class EnunciadoMedico(models.Model):
    medico = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='enunciados'
    )
    texto = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_registro']
        verbose_name = 'Enunciado Médico'
        verbose_name_plural = 'Enunciados del Médico'

    def __str__(self):
        return f'Enunciado de {self.medico.first_name} - {self.fecha_registro.strftime("%Y-%m-%d")}'

    