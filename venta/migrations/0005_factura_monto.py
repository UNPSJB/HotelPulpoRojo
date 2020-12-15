# Generated by Django 2.2.16 on 2020-12-10 23:26

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0004_remove_factura_fue_pagado'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='monto',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20),
        ),
    ]