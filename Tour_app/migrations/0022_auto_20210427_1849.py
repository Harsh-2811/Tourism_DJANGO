# Generated by Django 3.2 on 2021-04-27 13:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Tour_app', '0021_auto_20210427_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour_package',
            name='departure',
            field=models.DateField(default=datetime.datetime(2021, 4, 27, 13, 19, 26, 825136, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]