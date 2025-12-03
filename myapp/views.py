from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse, FileResponse, Http404
from django.conf import settings
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group


#este metodo retorna a la vista principal
def home(request):
    return render(request, "index.html")

def administrador(request):
    return render(request, "administrador.html")

def atencion(request):
    return render(request, "atencion.html")

def contactenos(request):
    return render(request, "contactenos.html")

def dashboard(request):
    return render(request, "Dashboards.html")

#este metodo retorna a la vista especialidades
def especialidades(request):
    return render(request, "especialidades.html")


#este método inicia la sesion del usuario
def loginup(request):
    if request.method == 'GET': #si se hace la petición al servidor entonces este devuelve la vista de login
        return render(request,'login.html')    
        
    else:
        user = authenticate(username=str.lower(request.POST['usuario']), 
                            password=request.POST['contrasena']) # almacena el usuario en una variable user y autentifica el usuario y contraseña enviados
        print({user})

        if user is None: #si el usuario y/o contraseña no existen entonces muestra nuevamente la vista login
            return render(request,'login.html', {
                    'error': 'El usuario o contraseña son incorrectos' #si no coincide el usuario y contraseña, imprime el error y renderiza la vista de login nuevamente  
            })
        else:
            login(request, user)
            # Redirigir según el grupo del usuario
            if user.is_active:
                # Verificar si pertenece al grupo Enfermeria
                if user.groups.filter(name='Enfermeria').exists():
                    return redirect('enfermeria')
                # Si es superusuario, al panel de administración
                elif user.is_superuser:
                    return redirect('admin_users')
                # Si es staff, a paciente
                elif user.is_staff:
                    return redirect('paciente')
            # Por defecto, a paciente
            return redirect('paciente')
        
    
def paciente(request):
    return render(request, "paciente.html")

def historia_gerontologica(request):
    if request.method == 'POST':
        
        # Guardar el paciente (Identificacion)
        paciente = Identificacion.objects.create(
            primer_nombre=request.POST.get('primer_nombre'),
            segundo_nombre=request.POST.get('segundo_nombre', ''),
            primer_apellido=request.POST.get('primer_apellido'),
            segundo_apellido=request.POST.get('segundo_apellido', ''),
            fecha_nacimiento=request.POST.get('fecha_nacimiento'),
            edad=request.POST.get('edad'),
            tipo_documento=request.POST.get('tipo_documento'),
            numero_documento_paciente=request.POST.get('numero_documento_paciente'),
            ciudad_residencia=request.POST.get('ciudad_residencia'),
            sexo=request.POST.get('sexo'),
            grupo_sanguineo=request.POST.get('grupo_sanguineo'),
            pais_nacimiento=request.POST.get('pais_nacimiento'),
            departamento_nacimiento=request.POST.get('departamento_nacimiento'),
            ciudad_nacimiento=request.POST.get('ciudad_nacimiento'),
            zona_residencia=request.POST.get('zona_residencia', 'U'),
        )

        # Guardar FamiliaAcudientes
        familia = FamiliaAcudientes.objects.create(
            paciente=paciente,
            acudiente_nombre=request.POST.get('acudiente_nombre'),
            acudiente_parentesco=request.POST.get('acudiente_parentesco'),
            acudiente_telefono=request.POST.get('acudiente_telefono', ''),
            acudiente_celular=request.POST.get('acudiente_celular'),
            acudiente_direccion=request.POST.get('acudiente_direccion'),
            acudiente_email=request.POST.get('acudiente_email'),
            acudiente_estado_civil=request.POST.get('acudiente_estado_civil'),
        )

        # Guardar GradoEscolaridad
        grado = GradoEscolaridad.objects.create(
            paciente=paciente,
            lee=request.POST.get('lee', '1'),
            escribe=request.POST.get('escribe', '1'),
            primaria_completa=request.POST.get('primaria_completa', '1'),
            secundaria_completa=request.POST.get('secundaria_completa', '1'),
            tecnico=request.POST.get('tecnico', ''),
            tecnologo=request.POST.get('tecnologo', ''),
            profesional=request.POST.get('profesional', ''),
            maestria=request.POST.get('maestria', ''),
            otros_estudios=request.POST.get('otros_estudios', ''),
        )

        # Guardar DatosSocioEconomicosForm
        socio = DatosSocioEconomicosForm.objects.create(
            paciente=paciente,
            actividad_desempenada=request.POST.get('actividad_desempenada'),
            ocupacion_actual=request.POST.get('ocupacion_actual'),
            aporte_familiar=request.POST.get('aporte_familiar', '1'),
            jubilacion=request.POST.get('jubilacion', '1'),
            renta_propia=request.POST.get('renta_propia', '1'),
            otros_ingresos=request.POST.get('otros_ingresos', ''),
        )

        # Guardar TipoFamilia
        tipo_familia = TipoFamilia.objects.create(
            paciente=paciente,
            tipo_familia=request.POST.get('tipo_familia'),
            otro_razon_tipo_familia=request.POST.get('otro_razon_tipo_familia', ''),
        )

        # Guardar SeguridadSocialSalud
        seguridad = SeguridadSocialSalud.objects.create(
            paciente=paciente,
            regimen_seguridad_social=request.POST.get('regimen_seguridad_social'),
            afiliacion_salud=request.POST.get('afiliacion_salud'),
            ips=request.POST.get('ips'),
        )

        # Guardar RelacionesIntrafamiliares
        relaciones = RelacionesIntrafamiliares.objects.create(
            paciente=paciente,
            tipo_relacion=request.POST.get('tipo_relacion'),
            maltrato=request.POST.get('maltrato', '0'),
            explicacion_relacion=request.POST.get('explicacion_relacion', ''),
            tipo_maltrato=request.POST.get('tipo_maltrato', ''),
        )

        # Guardar ProteccionExequial
        proteccion = ProteccionExequial.objects.create(
            paciente=paciente,
            proteccion_exequial=request.POST.get('proteccion_exequial', '0'),
            compania_proteccion_exequial=request.POST.get('compania_proteccion_exequial', ''),
        )

        # Guardar EspiritualidadReligion
        espiritualidad = EspiritualidadReligion.objects.create(
            paciente=paciente,
            grupo_religioso=request.POST.get('grupo_religioso', '1'),
            cual_grupo_religioso=request.POST.get('cual_grupo_religioso', ''),
            religion=request.POST.get('religion', ''),
            practica_religiosa=request.POST.get('practica_religiosa'),
            otros_practicas_religiosas=request.POST.get('otros_practicas_religiosas', ''),
        )

        # Guardar HabitosRutinas
        habitos = HabitosRutinas.objects.create(
            paciente=paciente,
            actividad_fisica=request.POST.get('actividad_fisica', '0'),
            tipo_actividad_fisica=request.POST.get('tipo_actividad_fisica', ''),
            actividades_recreativas=request.POST.get('actividades_recreativas', ''),
        )

        # Guardar Aspectos Fisicos
        aspectos_fisicos_salud = AspectosFisicosSalud.objects.create(
            paciente=paciente,
            estado_salud=request.POST.get('estado_salud', ''),
            explicacion_estado_salud=request.POST.get('explicacion_estado_salud', ''),
        )
        
        # Guardar adversidades a medicamentos
        adversidades_medicamentos = AdversidadesMedicamentos.objects.create(
            paciente=paciente,
            reacciones_adversas=request.POST.get('reacciones_adversas', '0'),
            descripcion_reacciones=request.POST.get('descripcion_reacciones', ''),
            alergias_medicamentos=request.POST.get('alergias_medicamentos', '0'),
            descripcion_alergias=request.POST.get('descripcion_alergias', ''),
            autprescripcion_medicamentos=request.POST.get('autprescripcion_medicamentos', '0'),            
        )
        
        # Guardar adversidades a alimentos
        adversidades_alimentos = AdversidadesAlimentos.objects.create(
            paciente=paciente,
            adversidad_alimentos=request.POST.get('adversidad_alimentos', '0'),
            descripcion_adversidad=request.POST.get('descripcion_adversidad', ''),
            alergias_alimentos=request.POST.get('alergias_alimentos', '0'),
            descripcion_alergias_alimentos=request.POST.get('descripcion_alergias_alimentos', ''),           
        )
        
        # Guardar antecedentes toxicos
        antecedentes_toxicos = AntecedentesToxicos.objects.create(
            paciente=paciente,
            consumo_sustancias=request.POST.get('consumo_sustancias', '0'),
            consumo_sustancias_tabaco=request.POST.get('consumo_sustancias_tabaco', '0'),
            consumo_sustancias_cafe=request.POST.get('consumo_sustancias_cafe', '0'),
            consumo_sustancias_psicoactivas=request.POST.get('consumo_sustancias_psicoactivas', '0'),
            frecuencia_consumo=request.POST.get('frecuencia_consumo'),
            cantidad_consumo=request.POST.get('cantidad_consumo'),
        )
        
        # Guardar revision por sistemas
        revision_por_sistemas = RevisionPorSistemas.objects.create(
            paciente=paciente,
            #sentidos
            cataratas=request.POST.get('cataratas', '0'),
            ceguera=request.POST.get('ceguera', '0'),
            presbicausia=request.POST.get('presbicausia', '0'),
            galucoma=request.POST.get('galucoma', '0'),
            sentidos_otros=request.POST.get('sentidos_otros'),
            
            #sistema cardiovascular
            infarto_miocardio=request.POST.get('infarto_miocardio', '0'),
            hta=request.POST.get('hta', '0'),
            insuficiencia_cardiaca=request.POST.get('insuficiencia_cardiaca', '0'),
            arteriosclerosis=request.POST.get('arteriosclerosis', '0'),
            cardiovascular_otros=request.POST.get('cardiovascular_otros'),
            
            #sistema respiratorio
            epoc=request.POST.get('epoc', '0'),
            bronquitis=request.POST.get('bronquitis', '0'),
            asma=request.POST.get('asma', '0'),
            neumonia=request.POST.get('neumonia', '0'),
            respiratorio_otros=request.POST.get('respiratorio_otros'),
            
            #sistema oseo muscular
            artritis=request.POST.get('artritis', '0'),
            osteoporosis=request.POST.get('osteoporosis', '0'),
            osteoartrosis=request.POST.get('osteoartrosis', '0'),
            lumbago=request.POST.get('lumbago', '0'),
            oseo_muscular_otros=request.POST.get('oseo_muscular_otros'),
            
            #sistema urinario
            anuria=request.POST.get('anuria', '0'),
            cistitis=request.POST.get('cistitis', '0'),
            prostatitis=request.POST.get('prostatitis', '0'),
            prolapso_genital=request.POST.get('prolapso_genital', '0'),
            incontinencia_urinaria=request.POST.get('incontinencia_urinaria', '0'),
            urinario_otros=request.POST.get('urinario_otros'),
            
            #sistema nervioso
            demencia_senil=request.POST.get('demencia_senil', '0'),
            alzheheimer=request.POST.get('alzheheimer', '0'),
            parkinson=request.POST.get('parkinson', '0'),
            esquizofrenia=request.POST.get('esquizofrenia', '0'),
            epilepsia=request.POST.get('epilepsia', '0'),
            nervioso_otros=request.POST.get('nervioso_otros'),
            
            #sistema endocrino
            diabetes_mellitus=request.POST.get('diabetes_mellitus', '0'),
            hipertiroidismo=request.POST.get('hipertiroidismo', '0'),
            hipotiroidismo=request.POST.get('hipotiroidismo', '0'),
            bocio=request.POST.get('bocio', '0'),
            endocrino_otros=request.POST.get('endocrino_otros'),
            
            #sistema tegumentario
            prurito=request.POST.get('prurito', '0'),
            urticaria=request.POST.get('urticaria', '0'),
            verrugas=request.POST.get('verrugas', '0'),
            quemaduras=request.POST.get('quemaduras', '0'),
            tegumentario_otros=request.POST.get('tegumentario_otros'),
            
            #sistema digestivo
            gastritis=request.POST.get('gastritis', '0'),
            diarrea=request.POST.get('diarrea', '0'),
            estrenimiento=request.POST.get('estrenimiento', '0'),
            ulcera_duodenal=request.POST.get('ulcera_duodenal', '0'),
            digestivo_otros=request.POST.get('digestivo_otros'),
            
            #tumores
            tejido_mamario=request.POST.get('tejido_mamario', '0'),
            sistema_digestivo=request.POST.get('sistema_digestivo', '0'),
            sistema_urinario=request.POST.get('sistema_urinario', '0'),
            tumores_otros=request.POST.get('tumores_otros'),
            
            #observaciones generales
            observaciones=request.POST.get('observaciones'),
        )
        
        # Guardar Evaluacion bucal
        evaluacion_bucal=EvaluacionBucal.objects.create(
            paciente=paciente,
            piezas_dentales_completas=request.POST.get('piezas_dentales_completas', '0'),
            piezas_dentales_incompletas=request.POST.get('piezas_dentales_incompletas', '0'),
            protesis=request.POST.get('protesis', '0'),
            observasiones=request.POST.get('observasiones'),
        )
        
        # Guardar sindromes y problemas geriatricos
        sindromes_geriatricos=SindromesProblemasGriatricos.objects.create(
            paciente=paciente,
            vertigo_mareo=request.POST.get('vertigo_mareo', '0'),
            delirio=request.POST.get('delirio', '0'),
            caidas=request.POST.get('caidas', '0'),
            numero_caidas=request.POST.get('numero_caidas'),
            sincopes=request.POST.get('sincopes', '0'),
            dolor_cronico=request.POST.get('dolor_cronico', '0'),
            depravacion_auditiva=request.POST.get('depravacion_auditiva', '0'),
            depravacion_visual=request.POST.get('depravacion_visual', '0'),
            insomio=request.POST.get('insomio', '0'),
            incontinencia_urinaria=request.POST.get('incontinencia_urinaria', '0'),
            otros_sindromes_problemas=request.POST.get('otros_sindromes_problemas'),
            observaciones_generales=request.POST.get('observaciones_generales'),
            observaciones_paciente=request.POST.get('observaciones_paciente'),      
        )
        
        # Guardar Evaluacion Bucal
        
        evaluacion_bucal = EvaluacionBucal.objects.create(
            paciente=paciente,
            piezas_dentales_completas=request.POST.get('piezas_dentales_completas', '0'),
            piezas_dentales_incompletas=request.POST.get('piezas_dentales_incompletas', '0'),
            protesis=request.POST.get('protesis', '0'),
            observasiones=request.POST.get('observasiones'),
        )
        
        # Guardar Sindromes y Problemas Geriatricos
        
        sindromes_geriatricos = SindromesProblemasGriatricos.objects.create(
            paciente=paciente,
            vertigo_mareo=request.POST.get('vertigo_mareo', '0'),
            delirio=request.POST.get('delirio', '0'),
            caidas=request.POST.get('caidas', '0'),
            numero_caidas=request.POST.get('numero_caidas'),
            sincopes=request.POST.get('sincopes', '0'),
            dolor_cronico=request.POST.get('dolor_cronico', '0'),
            depravacion_auditiva=request.POST.get('depravacion_auditiva', '0'),
            depravacion_visual=request.POST.get('depravacion_visual', '0'),
            insomio=request.POST.get('insomio', '0'),
            incontinencia_urinaria=request.POST.get('incontinencia_urinaria', '0'),
            otros_sindromes_problemas=request.POST.get('otros_sindromes_problemas'),
            observaciones_generales=request.POST.get('observaciones_generales'),
            observaciones_paciente=request.POST.get('observaciones_paciente'),      
        )
        
        # Guardar Validacion diaria Katz
        
        valoracion_diaria_katz = ValoracionVidaDiariaKatz.objects.create(
            paciente=paciente,
            alimentacion=request.POST.get('alimentacion'),
            bano=request.POST.get('bano'),
            continencia=request.POST.get('continencia'),
            movilidad=request.POST.get('movilidad'),
            uso_sanitarios=request.POST.get('uso_sanitarios'),
            vestido=request.POST.get('vestido'),
            puntuacion_total=request.POST.get('puntuacion_total'),
            observaciones=request.POST.get('observaciones'),
        )
        
        # Guardar ayudas ortopedicas
        
        ayudas_ortopedicas = AyudasOrtopedicas.objects.create(
            paciente=paciente,
            caminador=request.POST.get('caminador', '0'),
            caminador_observaciones=request.POST.get('caminador_observaciones', ''),
            muletas=request.POST.get('muletas', '0'),
            muletas_observaciones=request.POST.get('muletas_observaciones', ''),
            silla_de_ruedas=request.POST.get('silla_de_ruedas', '0'),
            silla_de_ruedas_observaciones=request.POST.get('silla_de_ruedas_observaciones', ''),
            baston=request.POST.get('baston', '0'),
            baston_observaciones=request.POST.get('baston_observaciones', ''),
            gafas=request.POST.get('gafas', '0'),
            gafas_observaciones=request.POST.get('gafas_observaciones', ''),
            audifonos=request.POST.get('audifonos', '0'),
            audifonos_observaciones=request.POST.get('audifonos_observaciones', ''),
            protesis=request.POST.get('protesis', '0'),
            protesis_observaciones=request.POST.get('protesis_observaciones', ''),
            otros=request.POST.get('otros', '0'),
            otros_observaciones=request.POST.get('otros_observaciones', ''),
        )
        
        # Guardar aspectos mentales
        
        aspectos_mentales = AspectosMentales.objects.create(
            paciente=paciente,
            psicosis=request.POST.get('psicosis', '0'),
            ansiedad=request.POST.get('ansiedad', '0'),
            problemas_intergeneracionales=request.POST.get('problemas_intergeneracionales', '0'),
            duelo=request.POST.get('duelo', '0'),
            afectivo_bipolar=request.POST.get('afectivo_bipolar', '0'),
            depresion=request.POST.get('depresion', '0'),
        )
        
        # Guardar Ideas Suicidas
        
        ideas_suicidas = IdeasSuicidas.objects.create(
            paciente=paciente,
            ideas_suicidas=request.POST.get('ideas_suicidas', '0'),
            explicacion_ideas_suicidas=request.POST.get('explicacion_ideas_suicidas'),
        )
        
        # Guardar Valoracion mental
        
        valoracion_mental = ValoracionMental.objects.create(
            paciente=paciente,
            fecha_hoy=request.POST.get('fecha_hoy'),
            dia_semana=request.POST.get('dia_semana'),
            lugar_actual=request.POST.get('lugar_actual'),
            numero_telefono=request.POST.get('numero_telefono'),
            direccion=request.POST.get('direccion'),
            edad=request.POST.get('edad'),
            lugar_nacimiento=request.POST.get('lugar_nacimiento'),
            apellido_madre=request.POST.get('apellido_madre'),
            restar_tres_en_tres=request.POST.get('restar_tres_en_tres'),
            # Valoracion cognitiva
            nivel_cognitivo=request.POST.get('nivel_cognitivo'),
            errores_totales=request.POST.get('errores_totales'),
            observaciones=request.POST.get('observaciones'),
        )
        
        # Guardar escala Yesavage
        
        escala_yesavage = EscalaYesavage.objects.create(
            paciente=paciente,
            satisfecho_vida=request.POST.get('satisfecho_vida', '0'),
            satisfecho_vida_valor=request.POST.get('satisfecho_vida_valor', '0'),
            renunciado_actividades=request.POST.get('renunciado_actividades', '0'),
            renunciado_actividades_valor=request.POST.get('renunciado_actividades_valor', '0'),
            vida_vacia=request.POST.get('vida_vacia', '0'),
            vida_vacia_valor=request.POST.get('vida_vacia_valor', '0'),
            aburrido=request.POST.get('aburrido', '0'),
            aburrido_valor=request.POST.get('aburrido_valor', '0'),
            alegre_optimista=request.POST.get('alegre_optimista', '0'),
            alegre_optimista_valor=request.POST.get('alegre_optimista_valor', '0'),
            temor_malo=request.POST.get('temor_malo', '0'),
            temor_malo_valor=request.POST.get('temor_malo_valor', '0'),
            feliz=request.POST.get('feliz', '0'),
            feliz_valor=request.POST.get('feliz_valor', '0'),
            desamparado=request.POST.get('desamparado', '0'),
            desamparado_valor=request.POST.get('desamparado_valor', '0'),
            quedarse_casa=request.POST.get('quedarse_casa', '0'),
            quedarse_casa_valor=request.POST.get('quedarse_casa_valor', '0'),
            fallos_memoria=request.POST.get('fallos_memoria', '0'),
            fallos_memoria_valor=request.POST.get('fallos_memoria_valor', '0'),
            agradable_vivo=request.POST.get('agradable_vivo', '0'),
            agradable_vivo_valor=request.POST.get('agradable_vivo_valor', '0'),
            duro_proyectos=request.POST.get('duro_proyectos', '0'),
            duro_proyectos_valor=request.POST.get('duro_proyectos_valor', '0'),
            lleno_energia=request.POST.get('lleno_energia', '0'),
            lleno_energia_valor=request.POST.get('lleno_energia_valor', '0'),
            situacion_angustiosa=request.POST.get('situacion_angustiosa', '0'),
            situacion_angustiosa_valor=request.POST.get('situacion_angustiosa_valor', '0'),
            economicamente_mejor=request.POST.get('economicamente_mejor', '0'),
            economicamente_mejor_valor=request.POST.get('economicamente_mejor_valor', '0'),
        )
        
        # Guardar Valoracion gerontologica general
        
        valoracion_gerontologica_general = ValoracionGerontologicaGeneral.objects.create(
            paciente=paciente,
            social_familiar=request.POST.get('social_familiar'),
            salud_fisica=request.POST.get('salud_fisica'),
            medicamentos_actuales=request.POST.get('medicamentos_actuales'),
            actividades_vida_diaria=request.POST.get('actividades_vida_diaria'),
            enfermedades_mentales=request.POST.get('enfermedades_mentales'),
            estado_salud_mental=request.POST.get('estado_salud_mental'),
            depresion=request.POST.get('depresion'),
        )
        
        # Guardar Seguimiento Gerontologico
        
        seguimiento_gerontologico = SeguimientoControlGerontologico.objects.create(
            paciente=paciente,
            observaciones_seguimiento=request.POST.get('observaciones_seguimiento'),
            fecha_seguimiento=request.POST.get('fecha_seguimiento'),
            nombre_profesional=request.POST.get('nombre_profesional'),
            firma_profesional=request.POST.get('firma_profesional'),
            registro_profesional=request.POST.get('registro_profesional'),
        )
        
        # Crear HistoriaGerontologica
        historia = HistoriaGerontologica.objects.create(
            fk_identificacion=paciente,
            fk_familia_acudientes=familia,
            fk_grado_escolaridad=grado,
            fk_datos_socio_economicos=socio,
            fk_tipo_familia=tipo_familia,
            fk_seguridad_social_salud=seguridad,
            fk_relaciones_intrafamiliares=relaciones,
            fk_proteccion_exequial=proteccion,
            fk_espiritualidad_religion=espiritualidad,
            fk_habitos_rutinas=habitos,
            fk_aspectos_fisicos_salud=aspectos_fisicos_salud,
            fk_adversidades_medicamentos=adversidades_medicamentos,
            fk_adversidades_alimentos=adversidades_alimentos,
            fk_antecedentes_toxicos=antecedentes_toxicos,
            fk_revision_por_sistemas=revision_por_sistemas,
            fk_evaluacion_bucal=evaluacion_bucal,
            fk_sindromes_geriatricos=sindromes_geriatricos,
            fk_valoracion_diaria_katz=valoracion_diaria_katz,
            fk_ayudas_ortopedicas=ayudas_ortopedicas,
            fk_aspectos_mentales=aspectos_mentales,
            fk_ideas_suicidas=ideas_suicidas,
            fk_valoracion_mental=valoracion_mental,
            fk_escala_yesavage=escala_yesavage,
            fk_valoracion_gerontologica_general=valoracion_gerontologica_general,
            fk_seguimiento_gerontologico=seguimiento_gerontologico,
            
            # Seccion solo para campos con relacion OneToOne
        )

        # Guardar medicamentos (ManyToManyField)
        nombre_medicamento = request.POST.getlist('nombre_medicamento[]')
        dosis= request.POST.getlist('dosis[]')
        observaciones= request.POST.getlist('observaciones[]')
        
        for i in range(len(nombre_medicamento)):
            nombre_medicamento = nombre_medicamento[i].strip()
            if not nombre_medicamento:
                continue
            
            medicamento = Medicamentos.objects.create(
                paciente=paciente,
                nombre_medicamento=nombre_medicamento,
                dosis=dosis[i],
                observaciones=observaciones[i],
            )
        historia.fk_medicamentos.add(medicamento)
        

        return redirect('historia_exito')  # página de éxito
    else:
        return render(request, "historia_gerontologica.html")


#este metodo retorna registra al usuario
def registro(request):
    if request.method == 'GET':#si se hace la petición al servidor entonces este devuelve la vista de registro
        return render(request, 'registro.html')
    else:
        #A continuación se almacenan lo datos escritos por el usuario en el formulario en variables
        correo = str.lower(request.POST.get('correo'))
        contrasena = request.POST.get('contrasena')
        confirmar_contrasena = request.POST.get('confirmar_contrasena')
        nombres = str.capitalize(str.lower(request.POST.get('nombres')))
        primer_apellido = str.capitalize(str.lower(request.POST.get('primer_apellido')))
        segundo_apellido = str.capitalize(str.lower(request.POST.get('segundo_apellido')))
        documentoid = str.upper(request.POST.get('documentoid'))
        celular = request.POST.get('celular')
        ciudad = str.capitalize(request.POST.get('ciudad'))
        direccion = request.POST.get('direccion')
        #profesional=str.capitalize(str.lower(request.POST.get('profesional')))
        

        #Se valida que las contraseñas coincidan
        if contrasena != confirmar_contrasena:
            return render(request, 'registro.html',{ 
                    'error': 'Las contraseñas no coinciden' #Error que indica que las contraseñas no coinciden
            })

        #Se valida que el correo no esté registrado
        if User.objects.filter(username=correo).exists(): #Se busca el correo en las tabla de la clase User si este existe devuelve un error
            return render(request, 'registro.html',{ 
                    'error': 'El correo electrónico ya está registrado' #Error que indica que el correo ya esta registrado
            })

        try:
            #Crea el usuario en la tabla User de Django
            user = User.objects.create_user(
                username=correo,  #Se crea el usuario a partir del correo
                email=correo,
                password=contrasena, #Se crea la contraseña del usuario 
                first_name=nombres,
                last_name=primer_apellido
            )
            user.save() #Se guarda el usuario en la tabla 

            #Crea el registro en la tabla TUsuario
            tuser = Usuario.objects.create(
                #nombre=nombres,
                #primer_apellido=primer_apellido,
                user=user,
                segundo_apellido=segundo_apellido,
                documento=documentoid,
                celular=celular,
                #correo=correo,
                ciudad=ciudad,
                direccion=direccion,
                #profesional=profesional
            )
            tuser.save() #Se guarda el usuario en la tabla

            #contrasena_hasheada = make_password(contrasena)
            """tlogin = TLogin(
                fk_iduser=tuser,
                contrasenaLogin=contrasena #contrasena_hasheada Se guarda la contraseña en la tabla de TLogin
            )
            tlogin.save() #Se guarda la contraseña en la tabla"""

            #Iniciar sesión automáticamente
            login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido.') #se le envia un mensaje al usuario de que el registro fue exitoso
            return redirect('home') #se redirecciona a la pagina de home

        except Exception as e:
             
            messages.error(request, f'Error al registrar el usuario: {str(e)}')#Se muestra especificamente el error ocurrido al intentar guardar el usuario y no lograrlo exitosamente
            return render(request, 'registro.html')
  
#este metodo cierra la sesion del usuario y redirecciona al usuario a la pagina principal 


def servicios(request):
    return render(request, "servicios.html")

#este metodo retorna a la vista quienes somos
def somos(request):
    return render(request, "Somos.html")

def terminos(request):
    return render(request, "terminos.html")

def cerrarSesion(request):
    logout(request)
    return redirect('home')


@login_required
def enfermeria(request):
    """Vista del módulo de enfermería - Dashboard con funcionalidades específicas"""
    # Verificar si el usuario pertenece al grupo Enfermeria
    if not request.user.groups.filter(name='Enfermeria').exists():
        messages.error(request, 'No tiene permisos para acceder a este módulo.')
        return redirect('home')
    
    # Obtener lista de pacientes (aquí puedes agregar filtros según tus necesidades)
    pacientes = Identificacion.objects.all()[:10]  # Limitar a 10 pacientes para el ejemplo
    
    # Estadísticas de ejemplo (puedes calcularlas dinámicamente)
    context = {
        'pacientes': pacientes,
        'pacientes_atendidos': pacientes.count(),
        'consultas_pendientes': 5,  # Ejemplo estático, calcula según tu lógica
        'signos_vitales': 12,  # Ejemplo estático
        'medicamentos_admin': 8,  # Ejemplo estático
    }
    
    return render(request, 'enfermeria.html', context)


@login_required
def evolucion_enfermeria(request):
    """Vista para el registro de evolución diaria de enfermería"""
    from datetime import date
    from .models import EvolucionDiariaEnfermeria
    
    # Verificar si el usuario pertenece al grupo Enfermeria
    if not request.user.groups.filter(name='Enfermeria').exists():
        messages.error(request, 'No tiene permisos para acceder a este módulo.')
        return redirect('home')
    
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            paciente_id = request.POST.get('paciente_id')
            paciente = Identificacion.objects.get(id=paciente_id)
            
            # Crear registro de evolución
            evolucion = EvolucionDiariaEnfermeria.objects.create(
                paciente=paciente,
                fecha=request.POST.get('fecha'),
                paso_el_dia=request.POST.get('paso_el_dia'),
                alimentacion=request.POST.get('alimentacion'),
                elimina=request.POST.get('elimina'),
                exonera=request.POST.get('exonera'),
                medicamentos=request.POST.get('medicamentos'),
                frecuencia_cardiaca=request.POST.get('frecuencia_cardiaca', ''),
                presion_arterial=request.POST.get('presion_arterial', ''),
                temperatura=request.POST.get('temperatura', ''),
                frecuencia_respiratoria=request.POST.get('frecuencia_respiratoria', ''),
                novedad=request.POST.get('novedad'),
                observacion=request.POST.get('observacion', ''),
                nombre_profesional=request.POST.get('nombre_profesional'),
                identificacion_profesional=request.POST.get('identificacion_profesional'),
                firma=request.POST.get('firma', ''),
                usuario_registro=request.user
            )
            
            messages.success(request, 'Registro de evolución guardado exitosamente.')
            return redirect('evolucion_enfermeria')
            
        except Exception as e:
            messages.error(request, f'Error al guardar el registro: {str(e)}')
    
    # Obtener lista de pacientes para el selector
    pacientes = Identificacion.objects.all().order_by('primer_nombre')
    
    # Obtener historial de evoluciones recientes
    evoluciones = EvolucionDiariaEnfermeria.objects.select_related('paciente').order_by('-fecha', '-fecha_registro')[:20]
    
    context = {
        'pacientes': pacientes,
        'evoluciones': evoluciones,
        'today': date.today().isoformat(),
    }
    
    return render(request, 'evolucion_enfermeria.html', context)


def descargar_manual_pdf(request):
    import os
    pdf_path = os.path.join(settings.BASE_DIR, 'manual_usuario.pdf')
    if not os.path.exists(pdf_path):
        # Respuesta amigable en lugar de 404 genérico
        return HttpResponse(
            "<h1>Manual PDF no encontrado</h1>"
            "<p>Genera el archivo ejecutando:</p>"
            "<pre>python scripts/build_manual_pdf.py --manual manual_usuario.md --images-dir docs/images --output manual_usuario.pdf --skip-missing</pre>"
            "<p>Luego vuelve a esta URL: <code>/manual.pdf</code></p>",
            status=404
        )
    return FileResponse(open(pdf_path, 'rb'), as_attachment=True, filename='manual_usuario.pdf')


# ------------------
# Admin: CRUD de usuarios
# ------------------


def is_admin_user(user):
    return user.is_active and (user.is_superuser or user.is_staff)


@login_required
@user_passes_test(is_admin_user)
def admin_users(request):
    User = get_user_model()
    users = User.objects.all().order_by('id')
    return render(request, 'lista_usuarios.html', {'users': users})


@login_required
@user_passes_test(is_admin_user)
def admin_user_create(request):
    User = get_user_model()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        errors = {}
        # validate basic form (password matching, etc.) first
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = request.POST.get('email', '').strip()
            first_name = request.POST.get('first_name', '').strip()
            telefono = request.POST.get('telefono', '').strip()

            # username uniqueness (case-insensitive)
            if User.objects.filter(username__iexact=username).exists():
                errors['username'] = 'El nombre de usuario ya existe.'

            # email validation and uniqueness
            if email:
                try:
                    validate_email(email)
                except ValidationError:
                    errors['email'] = 'Correo electrónico inválido.'
                else:
                    if User.objects.filter(email__iexact=email).exists():
                        errors['email'] = 'El correo ya está en uso.'
            else:
                errors['email'] = 'El correo electrónico es requerido.'

            # first_name required
            if not first_name:
                errors['first_name'] = 'El nombre (Nombres) es requerido.'

            # telefono basic format (digits, +, spaces, parentheses, dash)
            if telefono:
                if not re.match(r'^[0-9+\-\s()]{6,20}$', telefono):
                    errors['telefono'] = 'Teléfono con formato inválido.'

            if errors:
                profiles = ['Administrativo', 'Doctor', 'Paciente', 'Enfermeria']
                return render(request, 'formulario_usuario.html', {'form': form, 'create': True, 'profiles': profiles, 'errors': errors, 'prefill': request.POST})

            # no errors: save user
            user = form.save(commit=False)
            user.email = email
            user.first_name = first_name
            user.last_name = request.POST.get('last_name', '').strip()
            user.is_staff = 'is_staff' in request.POST
            user.is_superuser = 'is_superuser' in request.POST
            user.save()

            # if telefono provided, try to save in Usuario related model
            try:
                if telefono:
                    uobj = Usuario.objects.get(user=user)
                    uobj.celular = telefono
                    uobj.save()
            except Exception:
                pass

            profile = request.POST.get('profile')
            if profile:
                grp, _ = Group.objects.get_or_create(name=profile)
                user.groups.clear()
                user.groups.add(grp)
            messages.success(request, 'Usuario creado correctamente.')
            return redirect('admin_users')
        else:
            # form invalid (password mismatch etc.)
            errors = {'form': 'Revise los datos del formulario. Asegure que las contraseñas coincidan.'}
            profiles = ['Administrativo', 'Doctor', 'Paciente', 'Enfermeria']
            return render(request, 'formulario_usuario.html', {'form': form, 'create': True, 'profiles': profiles, 'errors': errors, 'prefill': request.POST})
    else:
        form = UserCreationForm()
    profiles = ['Administrativo', 'Doctor', 'Paciente', 'Enfermeria']
    return render(request, 'formulario_usuario.html', {'form': form, 'create': True, 'profiles': profiles})


@login_required
@user_passes_test(is_admin_user)
def admin_user_edit(request, user_id):
    User = get_user_model()
    user_obj = get_object_or_404(User, pk=user_id)
    profiles = ['Administrativo', 'Doctor', 'Paciente', 'Enfermeria']
    if request.method == 'POST':
        # actualizar username (permitir renombrar)
        nuevo_username = request.POST.get('username', user_obj.username).strip()
        if nuevo_username and nuevo_username != user_obj.username:
            # verificar unicidad
            if User.objects.filter(username__iexact=nuevo_username).exclude(pk=user_obj.pk).exists():
                messages.error(request, 'El nombre de usuario ya está en uso. Elija otro.')
                # volver a renderizar formulario con mensajes
                profiles = ['Administrativo', 'Doctor', 'Paciente', 'Enfermeria']
                current_group = user_obj.groups.first().name if user_obj.groups.first() else None
                telefono = ''
                try:
                    uobj = Usuario.objects.get(user=user_obj)
                    telefono = uobj.celular or ''
                except Exception:
                    telefono = ''
                return render(request, 'formulario_usuario.html', {'create': False, 'user_obj': user_obj, 'profiles': profiles, 'current_group': current_group, 'telefono': telefono, 'errors': {'username':'El nombre de usuario ya está en uso.'}})
        else:
            nuevo_username = user_obj.username

        # actualizar campos básicos
        user_obj.username = nuevo_username
        user_obj.email = request.POST.get('email', user_obj.email)
        user_obj.first_name = request.POST.get('first_name', user_obj.first_name)
        user_obj.last_name = request.POST.get('last_name', user_obj.last_name)
        # telefono (se guarda en el modelo Usuario relacionado, si existe)
        telefono = request.POST.get('telefono', '').strip()
        # actualizar flags
        user_obj.is_staff = 'is_staff' in request.POST
        user_obj.is_superuser = 'is_superuser' in request.POST
        # actualizar contraseña si se proporciona
        nueva_password = request.POST.get('password')
        if nueva_password:
            user_obj.set_password(nueva_password)
        user_obj.save()
        messages.success(request, 'Usuario actualizado correctamente.')
        # Guardar telefono en el modelo Usuario relacionado si existe
        try:
            uobj = Usuario.objects.get(user=user_obj)
            if telefono:
                uobj.celular = telefono
                uobj.save()
        except Exception:
            # si no existe Usuario relacionado, no forzamos la creación porque requiere campos obligatorios
            pass
        # asignar grupo
        profile = request.POST.get('profile')
        if profile:
            grp, _ = Group.objects.get_or_create(name=profile)
            user_obj.groups.clear()
            user_obj.groups.add(grp)
        return redirect('admin_users')
    else:
        # obtener grupo actual si existe
        current_group = None
        g = user_obj.groups.first()
        if g:
            current_group = g.name
    # obtener telefono si existe
    telefono = ''
    try:
        uobj = Usuario.objects.get(user=user_obj)
        telefono = uobj.celular or ''
    except Exception:
        telefono = ''
    return render(request, 'formulario_usuario.html', {'create': False, 'user_obj': user_obj, 'profiles': profiles, 'current_group': current_group, 'telefono': telefono})


@login_required
@user_passes_test(is_admin_user)
def admin_user_delete(request, user_id):
    User = get_user_model()
    user_obj = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user_obj.delete()
        return redirect('admin_users')
    return render(request, 'confirmar_borrado_usuario.html', {'user_obj': user_obj})