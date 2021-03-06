# Generated by Django 2.0.3 on 2018-07-12 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0031_auto_20180712_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bando',
            name='agevolazione_fatmol',
            field=models.IntegerField(default=3, help_text="Fattore di moltiplicazione del punteggio relativo all'anzianità di servizio nel caso di permanenza maggiore o uguale alla soglia stabilita.Serve per agevolare i dipendenti che da N anni non superano la progressione", verbose_name='Fattore moltiplicazione per bonus punteggio anzianità'),
        ),
        migrations.AlterField(
            model_name='bando',
            name='agevolazione_soglia_anni',
            field=models.IntegerField(default=3, help_text="Anzianità di servizio nella stessa posizione economica per usufruire della moltiplicazione del punteggio relativo all'anzianità di servizio", verbose_name='Anni permanenza per bonus punteggio anzianità'),
        ),
    ]
