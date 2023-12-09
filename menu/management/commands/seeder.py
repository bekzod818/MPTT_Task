from django.core.management.base import BaseCommand
from menu.models import MenuItem

class Command(BaseCommand):
    help = 'Adds menu items to the database'

    def handle(self, *args, **options):
        # Replace the data with your menu items
        menu_items_data = [
            {'title': 'Home', 'url': '/home/'},
            {'title': 'About', 'url': '/about/'},
            {'title': 'Services', 'url': '/services/'},
            {'title': 'Contact', 'url': '/contact/'},
            {'title': 'Services Submenu 1', 'url': '/services/submenu1/', 'parent_title': 'Services'},
            {'title': 'Services Submenu 2', 'url': '/services/submenu2/', 'parent_title': 'Services'},
            # Add more items as needed
        ]

        # Create a dictionary to store MenuItem objects by title
        menu_items_dict = {}

        # Create MenuItem objects without parents
        for item_data in menu_items_data:
            if 'parent_title' not in item_data:
                menu_item = MenuItem.objects.create(**item_data)
                menu_items_dict[item_data['title']] = menu_item

        # Create MenuItem objects with parents
        for item_data in menu_items_data:
            if 'parent_title' in item_data:
                parent_title = item_data.pop('parent_title')
                parent_item = menu_items_dict[parent_title]
                menu_item = MenuItem.objects.create(parent=parent_item, **item_data)
                menu_items_dict[item_data['title']] = menu_item

        self.stdout.write(self.style.SUCCESS('Successfully added menu items to the database.'))
