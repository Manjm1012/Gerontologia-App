from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Create test users for predefined clinical profiles and assign them to groups.'

    def handle(self, *args, **options):
        User = get_user_model()
        profiles = [
            ('Medico', 'medico_user'),
            ('Enfermeria', 'enfermeria_user'),
            ('Psicologo', 'psicologo_user'),
            ('Fisioterapia', 'fisioterapia_user'),
            ('Fonoaudiologia', 'fonoaudiologia_user'),
        ]

        created = []
        for display_name, username in profiles:
            group, _ = Group.objects.get_or_create(name=display_name)

            user, created_flag = User.objects.get_or_create(
                username=username,
                defaults={
                    'first_name': display_name,
                    'last_name': 'Test',
                    'email': f'{username}@example.com',
                }
            )

            if created_flag:
                user.set_password('ChangeMe123!')
                user.is_active = True
                user.save()

            user.groups.add(group)
            created.append((username, display_name, created_flag))

        self.stdout.write(self.style.SUCCESS('Created/ensured test users for profiles:'))
        for u, g, flag in created:
            status = 'created' if flag else 'existing'
            self.stdout.write(f'- {u} ({g}): {status}')

        self.stdout.write(self.style.WARNING('Default password for new users is "ChangeMe123!". Change it in production.'))
