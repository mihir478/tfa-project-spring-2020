# Generated by Django 3.0.5 on 2020-05-03 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20200502_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='sighting',
            name='primary_fur_color',
            field=models.CharField(choices=[('black', 'Black'), ('gray', 'Gray'), ('cinnamon', 'Cinnamon')], default='gray', max_length=50, verbose_name='Primary Fur Color'),
        ),
    ]
