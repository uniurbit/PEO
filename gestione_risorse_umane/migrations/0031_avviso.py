# Generated by Django 2.2.7 on 2019-11-11 09:51

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_risorse_umane', '0030_auto_20191017_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avviso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('titolo', models.CharField(help_text='Titolo Avviso', max_length=255)),
                ('corpo_del_testo', models.TextField(help_text='es. La partecipazione al Bando comporta...')),
                ('ordinamento', models.PositiveIntegerField(blank=True, default=0, help_text="posizione nell'ordinamento")),
                ('allegato', models.FileField(blank=True, null=True, upload_to='allegati_avvisi/%m-%Y/')),
                ('is_active', models.BooleanField(default=True, verbose_name='Visibile agli utenti')),
            ],
            options={
                'verbose_name': 'Avvisi',
                'verbose_name_plural': 'Avvisi',
                'ordering': ('ordinamento',),
            },
        ),
    ]
