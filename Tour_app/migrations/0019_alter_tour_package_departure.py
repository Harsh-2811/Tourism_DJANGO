# Generated by Django 3.2 on 2021-04-26 10:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Tour_app', '0018_auto_20210426_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour_package',
            name='departure',
            field=models.DateField(default=datetime.datetime(2021, 4, 26, 10, 46, 17, 404093, tzinfo=utc)),
        ),
    ]
