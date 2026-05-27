import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User

user = User.objects.filter(username='enfermero1').first()
if user:
    print(f'Usuario: {user.username}')
    print(f'Grupos: {[g.name for g in user.groups.all()]}')
    print(f'Activo: {user.is_active}')
    print(f'Email: {user.email}')
    
    # Verificar autenticación
    from django.contrib.auth import authenticate
    test_auth = authenticate(username='enfermero1', password='Enfermero123')
    print(f'Autenticación: {test_auth is not None}')
else:
    print('Usuario no encontrado')
