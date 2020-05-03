from django.http import HttpResponse
from django.shortcuts import render

from .models import Sighting


def index():
    return HttpResponse('Hello, User!')


def sightings_map(request):
    sightings = Sighting.objects.all()
    return render(request, 'tracker/map.html', {'sightings': sightings})


def sightings_list(request):
    sightings = Sighting.objects.all()
    return render(request, 'tracker/sightings.html', {'sightings': sightings})


def get_sighting(request, unique_squirrel_id):
    sighting = Sighting.objects.all().filter(unique_squirrel_id=unique_squirrel_id)[0]
    return render(request, 'tracker/sighting.html', {'sighting': sighting})


def stats(request):
    sightings = Sighting.objects.all()
    count = Sighting.objects.all().count()
    age_adult = len(sightings.filter(age='Adult')) / count * 100
    age_juvenile = len(sightings.filter(age='Juvenile')) / count * 100
    age_missing = 100 - age_adult - age_juvenile
    precision = 1
    age_adult_formatted = '{:.{}f}'.format(age_adult, precision)
    age_juvenile_formatted = '{:.{}f}'.format(age_juvenile, precision)
    age_missing_formatted = '{:.{}f}'.format(age_missing, precision)
    return render(request, 'tracker/stats.html', {
        'count': count,
        'age_adult': age_adult_formatted,
        'age_juvenile': age_juvenile_formatted,
        'age_missing': age_missing_formatted
    })
