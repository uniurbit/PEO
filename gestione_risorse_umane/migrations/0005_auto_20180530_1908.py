# Generated by Django 2.0.3 on 2018-05-30 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_risorse_umane', '0004_remove_dipendente_data_cessazione_contratto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dipendente',
            options={'ordering': ['matricola'], 'verbose_name': 'Dipendente', 'verbose_name_plural': 'Dipendenti'},
        ),
    ]