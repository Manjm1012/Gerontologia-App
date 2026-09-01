from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


ROLES = [
    'Medico',
    'Enfermeria',
    'Psicologo',
    'Fisioterapia',
    'Fonoaudiologia',
]


class Command(BaseCommand):
    help = 'Create default role groups for the application.'

    def handle(self, *args, **options):
        created_any = False
        for role in ROLES:
            group, created = Group.objects.get_or_create(name=role)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created group: {role}"))
                created_any = True
            else:
                self.stdout.write(f"Group already exists: {role}")

        if not created_any:
            self.stdout.write(self.style.NOTICE('No new groups were created.'))