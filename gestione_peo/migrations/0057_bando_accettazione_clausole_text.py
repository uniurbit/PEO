# Generated by Django 2.0.3 on 2018-11-09 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0056_auto_20181103_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='bando',
            name='accettazione_clausole_text',
            field=models.TextField(blank=True, help_text='es. Dichiaro di aver preso visione...', null=True),
        ),
    ]