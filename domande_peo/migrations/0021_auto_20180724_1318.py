# Generated by Django 2.0.3 on 2018-07-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domande_peo', '0020_modulodomandabando_punteggio_calcolato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulodomandabando',
            name='punteggio_calcolato',
            field=models.FloatField(blank=True, help_text='popolato da metodo .calcolo_punteggio', null=True),
        ),
    ]