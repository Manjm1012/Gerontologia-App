import secrets
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'List users and optionally assign temporary passwords to specified users.'

    def add_arguments(self, parser):
        parser.add_argument('--list', action='store_true', help='List all users and (hashed) password field')
        parser.add_argument('--set-temp', nargs='+', help='Usernames to assign a temporary password to')
        parser.add_argument('--password', type=str, help='If provided, use this password for all --set-temp users (otherwise generates random)')

    def handle(self, *args, **options):
        User = get_user_model()

        if not options['list'] and not options['set_temp']:
            raise CommandError('Use --list or --set-temp <user1> [user2 ...]')

        if options['list']:
            users = User.objects.all().order_by('username')
            if not users:
                self.stdout.write('No users found.')
                return
            for u in users:
                # We cannot reveal plaintext passwords; print metadata and stored hash
                self.stdout.write(f'{u.username}\t email={u.email or "-"}\t is_staff={u.is_staff}\t is_superuser={u.is_superuser}\t active={u.is_active}\t hash={u.password}')
            return

        # set-temp flow
        usernames = options['set_temp']
        provided = options.get('password')
        results = []
        for uname in usernames:
            try:
                u = User.objects.get(username=uname)
            except User.DoesNotExist:
                results.append((uname, 'NOT_FOUND', ''))
                continue

            if provided:
                pwd = provided
            else:
                # generate a reasonably strong temporary password
                pwd = 'Temp!' + secrets.token_urlsafe(6)

            u.set_password(pwd)
            u.save()
            results.append((uname, 'UPDATED', pwd))

        # Print results
        for uname, status, pwd in results:
            if status == 'UPDATED':
                self.stdout.write(self.style.SUCCESS(f'{uname} -> {pwd}'))
            else:
                self.stdout.write(self.style.ERROR(f'{uname} -> {status}'))

        self.stdout.write(self.style.WARNING('Warning: this command modifies user passwords in the database. Use with care.'))
