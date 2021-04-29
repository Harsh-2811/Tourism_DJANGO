# Generated by Django 3.2 on 2021-04-26 03:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Tour_app', '0013_auto_20210425_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour_itinerary',
            name='image',
        ),
        migrations.AddField(
            model_name='hotel',
            name='no_of_rating',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='hotel',
            name='rating',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='tour_itinerary',
            name='day_no',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='tour_package',
            name='departure',
            field=models.DateField(default=datetime.datetime(2021, 4, 26, 3, 11, 35, 408528, tzinfo=utc)),
        ),
    ]
