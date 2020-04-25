from django.db import models

# Create your models here.
class Sighting(models.Model):
    SHIFT_CHOICES = (
        ('am','AM'),
        ('pm','PM'),
    )
    x = models.FloatField('X')
    y = models.FloatField('Y')
    unique_squirrel_id = models.ForeignKey('Squirrel')
    hectare = models.CharField('Hectare', max_length=3)
    shift = models.CharField('Shift', max_length=2,choices=SHIFT_CHOICES )

#sighting = X,Y,Unique Squirrel ID,Hectare,Shift,Date,Hectare Squirrel Number,Age,Primary Fur Color,Highlight Fur Color,Combination of Primary and Highlight Color,Color notes,Location,Above Ground Sighter Measurement,Specific Location,Running,Chasing,Climbing,Eating,Foraging,Other Activities,Kuks,Quaas,Moans,Tail flags,Tail twitches,Approaches,Indifferent,Runs from,Other Interactions,Lat/Long,Zip Codes,Community Districts,Borough Boundaries,City Council Districts,Police Precincts