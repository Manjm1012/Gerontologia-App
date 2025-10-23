from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Usuario #TLogin
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.hashers import make_password


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