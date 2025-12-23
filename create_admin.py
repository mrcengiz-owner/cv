
import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cv_project.settings')
django.setup()

User = get_user_model()

def create_admin():
    username = 'admin'
    password = 'admin_password_123'
    email = 'admin@example.com'
    
    if not User.objects.filter(username=username).exists():
        print(f"Creating superuser: {username}")
        User.objects.create_superuser(username, email, password)
        print(f"Superuser created successfully!")
        print(f"Username: {username}")
        print(f"Password: {password}")
    else:
        u = User.objects.get(username=username)
        u.set_password(password)
        u.is_superuser = True
        u.is_staff = True
        u.save()
        print(f"Superuser {username} already exists. Password updated to: {password}")

if __name__ == '__main__':
    create_admin()
