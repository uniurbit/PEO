# Generated by Django 2.0.3 on 2018-06-19 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0021_auto_20180619_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bando',
            name='anni_servizio_minimi',
            field=models.IntegerField(default=3, help_text='Anni di servizio minimi per poter partecipare al bando', verbose_name='Anni di servizio minimi'),
        ),
    ]
