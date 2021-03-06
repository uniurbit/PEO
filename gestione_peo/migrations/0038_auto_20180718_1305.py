# Generated by Django 2.0.3 on 2018-07-18 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0037_auto_20180717_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moduloinserimentocampi',
            name='tipo',
            field=models.CharField(choices=[('CharField', 'caratteri'), ('TextField', 'descrizione lunga'), ('IntegerField', 'numero intero'), ('FloatField', 'numero con virgola'), ('_TitoloStudioField', 'selezione titolo di studio'), ('FileField', 'allegato pdf'), ('CheckBoxField', 'checkbox'), ('CustomSelectBoxField', 'menu a tendina'), ('CustomRadioBoxField', 'serie di opzioni'), ('ProtocolloField', 'protocollo (numero + data)'), ('DateField', 'data'), ('StartEndDateField', 'data inizio + data fine + checkbox "fino ad oggi"'), ('DurataComeInteroField', 'durata in anni/mesi/ore'), ('DataLowerThanBandoField', 'data non superiore al bando')], max_length=33),
        ),
    ]
