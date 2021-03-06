# Generated by Django 3.2 on 2021-04-28 13:15

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Tour_app', '0023_alter_tour_package_departure'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour_inquiry',
            old_name='departure_date',
            new_name='date',
        ),
        migrations.AddField(
            model_name='tour_package',
            name='Tour_ID',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='tour_package',
            name='departure',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Whole Year', 'Whole Year'), ('Jan', 'Jan'), ('Fab', 'Fab'), ('Mar', 'Mar'), ('April', 'April'), ('May', 'May'), ('Jun', 'Jun'), ('July', 'July'), ('Aug', 'Aug'), ('Sept', 'Sept'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], default=' ', max_length=62),
        ),
    ]
