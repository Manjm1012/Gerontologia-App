from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'List existing role groups.'

    def handle(self, *args, **options):
        groups = [g.name for g in Group.objects.all()]
        if groups:
            for g in groups:
                self.stdout.write(f"- {g}")
        else:
            self.stdout.write('No groups found.')
