import csv
from django.core.management.base import BaseCommand
from core.models import Test

class Command(BaseCommand):
    help = 'Loads data from a CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        with open(options['csv_file'], encoding='utf-8', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            for row in reader:
                id, name, descriptor, user_id = row
                Test.objects.create(id=id, name=name, descriptor=descriptor, user_id=user_id)