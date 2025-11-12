from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt


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
        elif user.is_superuser: #si el usuario existe en la base de datos y ademas coincide la contraseña, se redirige al usuario a la pagina de registro usuario
            login(request, user)
            return redirect('paciente')
        else:
            login(request, user)
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
            actividad_desempeñada=request.POST.get('actividad_desempeñada'),
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
            
            # ⚠️ agregar todos los demás OneToOneField aquí
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