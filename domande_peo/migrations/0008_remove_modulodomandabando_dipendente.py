# Generated by Django 2.0.3 on 2018-05-31 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domande_peo', '0007_remove_modulodomandabando_aiuto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modulodomandabando',
            name='dipendente',
        ),
    ]