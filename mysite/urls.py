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

#Aca se encuntran los enlaces que se importaron a partir de la clase myapp para que se pueda acceder a las rutas descritas en esa plantilla
urlpatterns = [
    # Rutas de administración personalizada (deben ir antes de admin.site.urls)
    path('admin/users/', views.admin_users, name='admin_users'),
    path('admin/users/create/', views.admin_user_create, name='admin_user_create'),
    path('admin/users/<int:user_id>/edit/', views.admin_user_edit, name='admin_user_edit'),
    path('admin/users/<int:user_id>/delete/', views.admin_user_delete, name='admin_user_delete'),

    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('administrador/', views.administrador, name='administrador'),
    path('atencion/', views.atencion, name='atencion'),
    path('contactenos/', views.contactenos, name='contactenos'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('especialidades/', views.especialidades, name='especialidades'),
    path('login/', views.loginup, name='login'),
    path('paciente/', views.paciente, name='paciente'),
    path('historia_gerontologica/', views.historia_gerontologica, name='historia_gerontologica'),
    path('login/registro/', views.registro, name='registro'),
    path('servicios/', views.servicios, name='servicios'),
    path('somos/', views.somos, name='somos'),
    path('terminos/', views.terminos, name='terminos'),
    path('logout/', views.cerrarSesion, name='logout'),
    path('manual.pdf', views.descargar_manual_pdf, name='manual_pdf'),
    path('enfermeria/', views.enfermeria, name='enfermeria'),
    path('enfermeria/evolucion/', views.evolucion_enfermeria, name='evolucion_enfermeria'),
    path('medico/', views.medico, name='medico'),
    path('medico/consulta-nueva/', views.medico_consulta_nueva, name='medico_consulta_nueva'),  
     path('medico/enunciado-nuevo/', views.medico_enunciado_nuevo, name='medico_enunciado_nuevo'),  
]

   



    
    
    
    
  
    
    
