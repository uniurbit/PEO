# Generated by Django 2.0.3 on 2018-06-04 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domande_peo', '0009_auto_20180602_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='domandabando',
            options={'ordering': ['-data_chiusura'], 'verbose_name': 'Domanda di partecipazione del Dipendente', 'verbose_name_plural': 'Domande di partecipazione dei Dipendenti'},
        ),
    ]