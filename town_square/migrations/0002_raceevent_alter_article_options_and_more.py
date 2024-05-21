# Generated by Django 5.0.6 on 2024-05-21 06:41

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('town_square', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaceEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('location', models.CharField()),
                ('event_name', models.CharField()),
                ('event_image', cloudinary.models.CloudinaryField(default='event_placeholder', max_length=255, verbose_name='image')),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=cloudinary.models.CloudinaryField(default='t7ycznl8fsl6irkde9pa', max_length=255, verbose_name='image'),
        ),
    ]
