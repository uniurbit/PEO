# Generated by Django 2.0.3 on 2018-06-04 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0011_auto_20180604_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='bando',
            name='slug',
            field=models.CharField(default='peo-2015', max_length=255),
            preserve_default=False,
        ),
    ]