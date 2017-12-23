import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from django.contrib.auth.models import User


# Cria um superuser
admin = User.objects.create(username='admin')
admin.set_password('demodemo')
admin.is_superuser = True
admin.is_staff = True
admin.save()
