# Generated by Django 2.0.13 on 2019-03-07 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0080_auto_20190227_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bando',
            name='protocollo_cod_titolario',
            field=models.CharField(blank=True, choices=[('9095', '7.1')], max_length=12, null=True, verbose_name='Codice titolario'),
        ),
    ]