from django.http import HttpResponse
from django.shortcuts import render

from .models import Sighting


def index():
    return HttpResponse('Hello, User!')


def sightings_map(request):
    sightings = Sighting.objects.all()
    return render(request, 'tracker/map.html', {'sightings': sightings})

def sighting_list(request):
    list_ = Sighting.objects.all()
    return render(request, 'tracker/list.html', {'sightings': list_})

def get_sighting(request, unique_squirrel_id):
    sighting = Sighting.objects.all().filter(unique_squirrel_id=unique_squirrel_id)[0]
    return render(request, 'tracker/sighting.html', {'sighting': sighting})
