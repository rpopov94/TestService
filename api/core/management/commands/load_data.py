import csv
from django.core.management.base import BaseCommand, CommandError
from core.models import Question

class Command(BaseCommand):
    help = 'Loads data from a CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        try:
            with open(csv_file_path, encoding='utf-8', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    id, title, q1, q2, q3, q4, answer, test_id = row
                    if not test_id: 
                        test_id = None
                    Question.objects.create(id=id, title=title, q1=q1, q2=q2, q3=q3, q4=q4, answer=answer, test_id=test_id)
            self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
        except FileNotFoundError:
            raise CommandError('File "%s" does not exist' % csv_file_path)