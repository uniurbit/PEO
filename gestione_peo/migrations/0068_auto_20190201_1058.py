# Generated by Django 2.0.3 on 2019-02-01 09:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0067_auto_20190201_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descrizioneindicatore',
            name='numero_inserimenti',
            field=models.IntegerField(default=1, help_text='Numero max inserimenti consentiti', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Numero max inserimenti'),
        ),
    ]
