# Generated by Django 2.0.3 on 2018-06-04 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestione_peo', '0009_auto_20180604_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClausoleBando',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('titolo', models.CharField(help_text='Titolo clausola (es: Privacy...', max_length=255)),
                ('descrizione', models.TextField(help_text='es. La partecipazione al Bando comporta...')),
                ('ordinamento', models.PositiveIntegerField(help_text="posizione nell'ordinamento")),
                ('is_active', models.BooleanField(default=True, verbose_name='redazione')),
                ('bando', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestione_peo.Bando')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created-gestione_peo_clausolebando_related+', related_query_name='created-gestione_peo_clausolebandos+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified-gestione_peo_clausolebando_related+', related_query_name='modified-gestione_peo_clausolebandos+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Clausola Bando',
                'verbose_name_plural': 'Clausole Bando',
            },
        ),
    ]
