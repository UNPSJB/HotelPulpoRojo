# Generated by Django 3.1.1 on 2020-10-05 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='habitacion',
            unique_together={('hotel', 'numero')},
        ),
    ]