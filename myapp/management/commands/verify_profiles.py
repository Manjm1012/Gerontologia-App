from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'List groups and users assigned to each profile group.'

    def handle(self, *args, **options):
        groups = Group.objects.all().order_by('name')
        if not groups:
            self.stdout.write('No groups found in the system.')
            return

        for g in groups:
            users = g.user_set.all()
            self.stdout.write(f'Group: {g.name} (users: {users.count()})')
            for u in users:
                self.stdout.write(f' - {u.username} ({u.get_full_name() or "-"})')

        self.stdout.write(self.style.SUCCESS('Profile verification complete.'))
