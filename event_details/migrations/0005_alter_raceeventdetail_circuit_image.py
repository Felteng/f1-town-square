# Generated by Django 5.0.6 on 2024-05-24 10:54

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_details', '0004_rename_raceeventdetails_raceeventdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raceeventdetail',
            name='circuit_image',
            field=cloudinary.models.CloudinaryField(default='circuit_default', max_length=255, verbose_name='Circuit layout'),
        ),
    ]
