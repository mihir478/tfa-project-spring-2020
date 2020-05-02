# Generated by Django 3.0.5 on 2020-05-02 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sighting',
            old_name='y',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='sighting',
            old_name='x',
            new_name='longitude',
        ),
        migrations.RemoveField(
            model_name='sighting',
            name='approaches',
        ),
        migrations.RemoveField(
            model_name='sighting',
            name='chasing',
        ),
        migrations.RemoveField(
            model_name='sighting',
            name='climbing',
        ),
        migrations.RemoveField(
            model_name='sighting',
            name='eating',
        ),
        migrations.RemoveField(
            model_name='sighting',
            name='foraging',
        ),
        migrations.RemoveField(
            model_name='sighting',
            name='hectare',
        ),
        migrations.RemoveField(
            model_name='sighting',
            name='indifferent',
        ),
        migrations.RemoveField(
            model_name='sighting',
            name='kuks',
        ),
        migrations.RemoveField(
            model_name='sighting',
            name='location',
        ),
        migrations.RemoveField(
            model_name='sighting',
            name='moans',
        ),
        migrations.RemoveField(
            model_name='sighting',
            name='other_activities',
        ),
        migrations.RemoveField(
            model_name='sighting',
            name='primary_fur_color',
        ),
        migrations.RemoveField(
            model_name='sighting',
            name='quaas',
        ),
        migrations.RemoveField(
            model_name='sighting',
            name='running',
        ),
        migrations.RemoveField(
            model_name='sighting',
            name='runs_from',
        ),
        migrations.RemoveField(
            model_name='sighting',
            name='specific_location',
        ),
        migrations.RemoveField(
            model_name='sighting',
            name='tail_flags',
        ),
        migrations.RemoveField(
            model_name='sighting',
            name='tail_twitches',
        ),
    ]
