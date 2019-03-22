# Generated by Django 2.0.3 on 2019-01-31 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_risorse_umane', '0028_dipendente_disattivato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dipendente',
            name='ruolo',
            field=models.CharField(blank=True, choices=[('ND', 'ND - Personale non docente'), ('DC', 'DC - Dirigente a contratto'), ('NB', 'NB - ND Centro Residenziale'), ('D0', 'D0 - Dirigenti Superiori'), ('NM', 'NM - Non docenti a tempo det.-Tesoro'), ('NG', 'NG - Addetti ufficio stampa'), ('PO', 'PO - Professori Ordinari'), ('PA', 'PA - Professori Associati'), ('RU', 'RU - Ricercatori Universitari'), ('RM', 'RM - Ricercatori a tempo det-Tesoro'), ('RD', 'RD - Ricercatori Legge 240/10 - t.det.')], default='', max_length=33),
        ),
    ]