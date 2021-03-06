# Generated by Django 2.0.3 on 2018-05-30 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0002_auto_20180530_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='bando',
            name='pubblicato',
            field=models.BooleanField(default=False, help_text='Se selezionato sarà visibile al pubblico'),
        ),
        migrations.AlterField(
            model_name='bando',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Se attivo sarà Bando di riferimento per calcolo idoneità domanda peo per i dipendenti'),
        ),
    ]
