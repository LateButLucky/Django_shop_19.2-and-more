from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Load data into the database, clearing old data first'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing old data...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write('Loading new data...')
        call_command('loaddata', 'catalog/fixtures/categories_data.json')

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
