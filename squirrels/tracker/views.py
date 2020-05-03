from django.http import HttpResponse
from django.shortcuts import render

from .models import Sighting
import json

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

    color_gray = len(sightings.filter(primary_fur_color='Gray'))/count * 100
    color_cinnamon = len(sightings.filter(primary_fur_color='Cinnamon')) / count * 100
    color_black = len(sightings.filter(primary_fur_color='Black')) / count * 100
    color_missing = 100 - color_gray - color_cinnamon - color_black
    color_gray_formatted = '{:.{}f}'.format(color_gray, precision)
    color_cinnamon_formatted = '{:.{}f}'.format(color_cinnamon, precision)
    color_black_formatted = '{:.{}f}'.format(color_black, precision)
    color_missing_formatted = '{:.{}f}'.format(color_missing, precision)

    date_dict = dict.fromkeys(map(lambda s: s.date.strftime('%Y-%m-%d'), sightings), 0)
    for sighting in sightings:
        date_str = sighting.date.strftime('%Y-%m-%d')
        if date_dict[date_str]:
            date_dict[date_str] += 1
        else:
            date_dict[date_str] = 1
    sighting_timeseries = json.dumps(date_dict)

    return render(request, 'tracker/stats.html', {
        'count': count,
        'age_adult': age_adult_formatted,
        'age_juvenile': age_juvenile_formatted,
        'age_missing': age_missing_formatted,
        'color_gray': color_gray_formatted,
        'color_black': color_black_formatted,
        'color_cinnamon': color_cinnamon_formatted,
        'color_missing': color_missing_formatted,
        'sighting_timeseries': sighting_timeseries
    })
