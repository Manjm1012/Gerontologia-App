import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from django.contrib.auth.models import Group

groups = [g.name for g in Group.objects.all()]
print(groups)
