# Generated by Django 2.0.3 on 2018-11-19 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_risorse_umane', '0024_auto_20181119_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dipendente',
            name='data_ultima_progressione_manuale',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]