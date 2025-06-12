import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')  # ajuste se necessário
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'fdisugf123@gmail.com', '1623q12j')
    print("Superusuário criado.")
else:
    print("Superusuário já existe.")
