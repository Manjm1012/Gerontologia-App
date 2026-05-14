"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import ver_historia



#Aca se encuntran los enlaces que se importaron a partir de la clase myapp para que se pueda acceder a las rutas descritas en esa plantilla
urlpatterns = [
    path('', views.home, name='home'),
    path('administrador/', views.administrador, name='administrador'),
    # Rutas de administración de usuarios (ANTES del admin de Django)
    path('administrador/usuarios/', views.admin_users, name='admin_users'),
    path('administrador/usuarios/crear/', views.admin_user_create, name='admin_user_create'),
    path('administrador/usuarios/<int:user_id>/editar/', views.admin_user_edit, name='admin_user_edit'),
    path('administrador/usuarios/<int:user_id>/eliminar/', views.admin_user_delete, name='admin_user_delete'),
    path('admin/', admin.site.urls),
    path('atencion/', views.atencion, name='atencion'),
    path('contactenos/', views.contactenos, name='contactenos'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('especialidades/', views.especialidades, name='especialidades'),
    path('login/', views.loginup, name='login'),
    path('paciente_registro/', views.paciente_registro, name='paciente_registro'),
    path('historia_gerontologica/', views.historia_gerontologica, name='historia_gerontologica'),
    path('login/registro/', views.registro, name='registro'),
    path('servicios/', views.servicios, name='servicios'),
    path('somos/', views.somos, name='somos'),
    path('terminos/', views.terminos, name='terminos'),
    path('logout/', views.cerrarSesion, name='logout'),
    path('manual.pdf', views.descargar_manual_pdf, name='manual_pdf'),
    path('enfermeria/', views.enfermeria, name='enfermeria'),
    path('enfermeria/medicamentos/', views.control_medicamentos, name='control_medicamentos'),
    path('enfermeria/evolucion/', views.evolucion_enfermeria, name='evolucion_enfermeria'),
    path('enfermeria/historial/', views.historial_evoluciones, name='historial_evoluciones'),
    # path('perfil_paciente/', views.perfil_paciente, name='perfil_paciente'),
    path('paciente/', views.perfil_paciente, name='perfil_paciente_demo'),
    path("paciente/<int:paciente_id>/", views.perfil_paciente, name="perfil_paciente"),
    path('medico/', views.medico, name='medico'),
    path('medico/consulta-nueva/', views.medico_consulta_nueva, name='medico_consulta_nueva'),  
    path('medico/enunciado-nuevo/', views.medico_enunciado_nuevo, name='medico_enunciado_nuevo'),
    #hiatorial geriatico y pdf
    path('enfermeria/historia/', views.buscar, name='buscar_historial'),


    path('historia/<int:id>/', ver_historia, name='ver_historia'),



]

    
    
