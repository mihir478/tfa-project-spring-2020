from django.http import HttpResponse
from django.shortcuts import render

from .models import Sighting


def index():
    return HttpResponse('Hello, User!')


def sightings_map(request):
    sightings = Sighting.objects.all()
    return render(request, 'tracker/map.html', {'sightings': sightings})


def get_sighting(request, unique_squirrel_id):
    print(unique_squirrel_id)
    sighting = Sighting.objects.get(unique_squirrel_id=unique_squirrel_id)
    print(sighting)
    return render(request, 'tracker/sighting.html', {'sighting': sighting})
