# Generated by Django 5.0.6 on 2024-05-23 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_details', '0003_rename_detailedraceevent_raceeventdetails'),
        ('town_square', '0004_alter_raceevent_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RaceEventDetails',
            new_name='RaceEventDetail',
        ),
    ]
