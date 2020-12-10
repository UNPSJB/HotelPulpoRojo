# Generated by Django 2.2.16 on 2020-12-10 23:09

import datetime
import django.core.validators
from django.db import migrations, models
import hotel.models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_hotel_encargado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacion',
            name='numero',
            field=models.PositiveSmallIntegerField(default=101, validators=[django.core.validators.MinValueValidator(101), django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AlterField(
            model_name='temporadaalta',
            name='fin',
            field=models.DateField(default=datetime.datetime.today, validators=[hotel.models.validate_date_not_incorrect]),
        ),
        migrations.AlterField(
            model_name='temporadaalta',
            name='inicio',
            field=models.DateField(default=datetime.datetime.today, validators=[hotel.models.validate_date_not_in_past]),
        ),
    ]
