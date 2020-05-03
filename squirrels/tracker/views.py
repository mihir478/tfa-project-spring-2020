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
    count = Sighting.objects.all().count()
    age_adult = Sighting.objects.all().filter(age='adult').count()/count*100
    age_juv = Sighting.objects.all().filter(age='juvenile').count()/count*100

    return render(request,'tracker/stats.html', {'count': count,'adult': age_adult,'juvenile': age_juv})
