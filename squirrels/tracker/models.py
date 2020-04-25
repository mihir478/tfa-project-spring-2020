from django.db import models

# Create your models here.
class Sighting(models.Model):
    SHIFT_CHOICES = (
        ('am', 'AM'),
        ('pm', 'PM'),
    )
    AGE_CHOICES = (
        ('adult', 'Adult'),
        ('juvenile', 'Juvenile'),
    )
    FUR_CHOICES = (
        ('gray', 'Gray'),
        ('cinnamon', 'Cinnamon'),
        ('black', 'Black'),
    )
    LOCATION_CHOICES = (
        ('ground_plane', 'Ground Plane'),
        ('above_ground', 'Above Ground'),
    )
    x = models.FloatField('X')
    y = models.FloatField('Y')
    unique_squirrel_id = models.CharField('Squirrel', max_length=20)
    hectare = models.CharField('Hectare', max_length=3)
    shift = models.CharField('Shift', max_length=2, choices=SHIFT_CHOICES)
    date = models.DateField('Date')
    age = models.CharField('Age', max_length=50, choices=AGE_CHOICES)
    primary_fur_color = models.CharField('Primary Fur Color', max_length=50, choices=FUR_CHOICES)
    location = models.CharField('Location', max_length=50, choices=LOCATION_CHOICES)
    specific_location = models.CharField('Specific Location', max_length=100)
    running = models.BooleanField('Running')
    chasing = models.BooleanField('Chasing')
    climbing = models.BooleanField('Climbing')
    eating = models.BooleanField('Eating')
    foraging = models.BooleanField('Foraging')
    other_activities = models.CharField('Other Activities', max_length=100)
    kuks = models.BooleanField('Kuks')
    quaas = models.BooleanField('Quaas')
    moans = models.BooleanField('Moans')
    tail_flags = models.BooleanField('Tail flags')
    tail_twitches = models.BooleanField('Tail twitches')
    approaches = models.BooleanField('Approaches')
    indifferent = models.BooleanField('Indifferent')
    runs_from = models.BooleanField('Runs from')


