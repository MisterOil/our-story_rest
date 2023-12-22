from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create an initial superuser for the application'

    def handle(self, *args, **options):
        if not User.objects.filter(username='MisterOil').exists():
            User.objects.create_superuser('MisterOil', 'molirun91@gmail.com', 'Oil34543.')
            self.stdout.write(self.style.SUCCESS('Successfully created superuser'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))