# Generated by Django 3.2 on 2021-05-01 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tour_app', '0027_room_no_of_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('no_of_rooms', models.IntegerField()),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tour_app.hotel')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tour_app.room')),
            ],
        ),
    ]