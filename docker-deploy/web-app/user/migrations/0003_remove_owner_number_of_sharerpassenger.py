# Generated by Django 4.1.5 on 2023-02-07 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_owner_number_of_sharerpassenger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='Number_of_SharerPassenger',
        ),
    ]
