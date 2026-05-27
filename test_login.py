import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth import authenticate

# Probar autenticación con el usuario enfermero
print('Probando autenticación:')
print('-' * 50)

# Probar exactamente como está en el código
usuario_input = 'enfermero1'
password_input = 'Enfermero123'

# Como lo hace el código (con lower)
usuario_lower = str.lower(usuario_input)
print(f'Usuario (lower): {usuario_lower}')
print(f'Password: {password_input}')

user = authenticate(username=usuario_lower, password=password_input)
print(f'Resultado: {user}')

if user:
    print(f'\n✓ Autenticación exitosa')
    print(f'Username: {user.username}')
    print(f'Grupos: {[g.name for g in user.groups.all()]}')
    print(f'Es superusuario: {user.is_superuser}')
    print(f'Es staff: {user.is_staff}')
    print(f'Está activo: {user.is_active}')
else:
    print('\n✗ Autenticación fallida')
    
    # Verificar si el usuario existe
    from django.contrib.auth.models import User
    exists = User.objects.filter(username=usuario_lower).exists()
    print(f'Usuario existe: {exists}')
