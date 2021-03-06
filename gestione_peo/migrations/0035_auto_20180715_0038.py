# Generated by Django 2.0.3 on 2018-07-14 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0034_auto_20180714_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='bando',
            name='protocollo_required',
            field=models.BooleanField(default=True, help_text='Se attivo la domanda di partecipazione al bando dovrà necessariamente essere protocollata in fase di chiusura', verbose_name='Protocollo domanda obbligatorio'),
        ),
        migrations.AlterField(
            model_name='descrizioneindicatore',
            name='is_required',
            field=models.BooleanField(default=False, help_text='Se attivo la domanda non potrà essere presentata senza la presenza di questo Indicatore.', verbose_name='Inserimento in domanda obbigatorio'),
        ),
        migrations.AlterField(
            model_name='moduloinserimentocampi',
            name='tipo',
            field=models.CharField(choices=[('CharField', 'caratteri'), ('TextField', 'descrizione lunga'), ('IntegerField', 'numero intero'), ('FloatField', 'numero con virgola'), ('_TitoloStudioField', 'selezione titolo di studio'), ('DateField', 'data'), ('StartEndDateField', 'data inizio + data fine + checkbox "fino ad oggi"'), ('FileField', 'allegato pdf'), ('CheckBoxField', 'checkbox'), ('CustomSelectBoxField', 'menu a tendina'), ('CustomRadioBoxField', 'serie di opzioni'), ('ProtocolloField', 'protocollo (numero + data)'), ('DurataComeInteroField', 'durata in anni/mesi/ore')], max_length=33),
        ),
    ]
