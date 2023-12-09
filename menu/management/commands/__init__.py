# seeds.py

from django.core.management.base import BaseCommand
from menu.models import Menu, MenuItem
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample menu data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding the database...'))

        # Create menus
        menu1 = Menu.objects.create(title='Main Menu', slug='main-menu')
        menu2 = Menu.objects.create(title='Footer Menu', slug='footer-menu')

        # Create menu items
        MenuItem.objects.create(menu=menu1, title='Home', url='/')
        MenuItem.objects.create(menu=menu1, title='Blog', url='/blog/')
        MenuItem.objects.create(menu=menu1, title='Contact', url='/contact/')

        MenuItem.objects.create(menu=menu2, title='About Us', url='/about/')
        MenuItem.objects.create(menu=menu2, title='Privacy Policy', url='/privacy/')

        # You can add more items as needed

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
