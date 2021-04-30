# Generated by Django 3.2 on 2021-04-24 11:19

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc
import re


class Migration(migrations.Migration):

    dependencies = [
        ('Tour_app', '0002_alter_tour_package_departure'),
    ]

    operations = [
        migrations.AddField(
            model_name='countries',
            name='places',
            field=models.CharField(default='', max_length=200, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
        migrations.AlterField(
            model_name='tour_package',
            name='departure',
            field=models.DateField(default=datetime.datetime(2021, 4, 24, 11, 19, 36, 589514, tzinfo=utc)),
        ),
    ]