# Generated by Django 2.0.3 on 2019-02-04 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0076_auto_20190204_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruolidisabilitati_descrizioneindicatore',
            name='ruolo',
            field=models.CharField(blank=True, choices=[('ND', 'ND - Personale non docente'), ('DC', 'DC - Dirigente a contratto'), ('NB', 'NB - ND Centro Residenziale'), ('D0', 'D0 - Dirigenti Superiori'), ('NM', 'NM - Non docenti a tempo det.-Tesoro'), ('NG', 'NG - Addetti ufficio stampa'), ('PO', 'PO - Professori Ordinari'), ('PA', 'PA - Professori Associati'), ('RU', 'RU - Ricercatori Universitari'), ('RM', 'RM - Ricercatori a tempo det-Tesoro'), ('RD', 'RD - Ricercatori Legge 240/10 - t.det.')], max_length=50, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='ruolidisabilitati_descrizioneindicatore',
            unique_together={('descrizione_indicatore', 'ruolo')},
        ),
    ]