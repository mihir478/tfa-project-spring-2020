from django.db import models

# Create your models here.
class Sighting(models.Model):
    SHIFT_CHOICES = (
        ('am', 'AM'),
        ('pm', 'PM'),
    )
    AGE_CHOICES = (
        ('adult','Adult'),
        ('juvenile','Juvenile'),
    )
    FUR_CHOICES = (
        ('gray','Gray'),
        ('cinnamon','Cinnamon'),
        ('black','Black'),
    )
    LOCATION_CHOICES = (
        ('ground_plane', 'Ground Plane'),
        ('above_ground', 'Above Ground'),
    )
    x = models.FloatField('X')
    y = models.FloatField('Y')
    unique_squirrel_id = models.ForeignKey('Squirrel')
    hectare = models.CharField('Hectare', max_length=3)
    shift = models.CharField('Shift', max_length=2,choices=SHIFT_CHOICES )
    date = models.dateField('Date')
    age = models.CharField('Age',max_length=50,choices=AGE_CHOICES)
    primary_fur_color = models.CharField('Primary Fur Color',max_length=50,choices=FUR_CHOICES)
    location = models.CharField('Location',max_length=50,choices=LOCATION_CHOICES)
    sepcific_location = models.CharField('Specific Location',max_length=100)
    running = models.NullBooleanField('Running')
    chasing = models.NullBooleanField('Chasing')
    climbing = models.NullBooleanField('Climbing')
    eating = models.NullBooleanField('Eating')
    foraging = models.NullBooleanField('Foraging')
    other_activities = models.CharField('Other Activities', max_length=100)
    kuks = models.NullBooleanField('Kuks')
    quaas = models.NullBooleanField('Quaas')
    moans = models.NullBooleanField('Moans')
    tail_flags = models.NullBooleanField('Tail_flags')
    tail_twitches = models.NullBooleanField('Tail twitches')
    approaches = models.NullBooleanField('Approaches')
    indifferent = models.NullBooleanField('Indifferent')
    runs_from = models.NullBooleanField('Runs from')


