# Generated by Django 5.0.6 on 2024-06-11 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_details', '0010_alter_raceeventcomment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raceeventdetail',
            name='circuit_name',
            field=models.CharField(max_length=70),
        ),
    ]