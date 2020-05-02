from django.db import models


class Sighting(models.Model):
    SHIFT_CHOICES = (
        ('am', 'AM'),
        ('pm', 'PM'),
    )
    AGE_CHOICES = (
        ('adult', 'Adult'),
        ('juvenile', 'Juvenile'),
    )
    longitude = models.FloatField('Longitude')
    latitude = models.FloatField('Latitude')
    unique_squirrel_id = models.CharField('Unique Squirrel ID', max_length=20)
    shift = models.CharField('Shift', max_length=2, choices=SHIFT_CHOICES)
    date = models.DateField('Date')
    age = models.CharField('Age', max_length=50, choices=AGE_CHOICES)


