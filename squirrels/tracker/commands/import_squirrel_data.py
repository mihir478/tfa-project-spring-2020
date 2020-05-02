import csv

from django.core.management.base import BaseCommand
from django.utils import timezone
from squirrels.models import Sighting

class Command(BaseCommand):
    help = 'Import squirrel data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        sightings = []
        for dict_ in data:
            sightings.append(Sighting(
                longitude=float(dict_['X']),
                latitude=float(dict_['Y']),
                unique_squirrel_id=dict_['Unique Squirrel ID'],
                shift=dict_['Shift'].lower(),
                date=timezone.datetime.strptime(dict_['Date'], '%m%d%Y').date(),
                age=dict_['Age']
            ))

        Sighting.objects.bulk_create(sightings)
