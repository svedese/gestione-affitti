# Generated by Django 2.0.3 on 2018-04-06 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amministratore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(blank=True, max_length=10)),
                ('nome', models.CharField(help_text='*', max_length=100)),
                ('cognome', models.CharField(help_text='*', max_length=100)),
                ('sesso', models.CharField(choices=[('M', 'Maschio'), ('F', 'Femmina')], help_text='*', max_length=1)),
                ('nascita_data', models.DateField(help_text='*', verbose_name='data di nascita')),
                ('nascita_luogo', models.CharField(help_text='*', max_length=100, verbose_name='luogo di nascita')),
                ('codice_fiscale', models.CharField(help_text='max_length=16 *', max_length=16)),
                ('partita_iva', models.CharField(help_text='*', max_length=20)),
            ],
            options={
                'verbose_name': 'amministratore',
                'verbose_name_plural': 'amministratori',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Condominio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='*', max_length=100)),
                ('codice_fiscale', models.CharField(help_text='max_length=16 *', max_length=16)),
                ('amministratore', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Amministratore')),
            ],
            options={
                'verbose_name': 'condominio',
                'verbose_name_plural': 'condomini',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='ContrattoLocazione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decorrenza', models.PositiveSmallIntegerField(help_text='numero mesi *')),
                ('durata', models.PositiveSmallIntegerField(help_text='numero mesi *')),
                ('data_stipula', models.DateField(help_text='*')),
                ('canone_importo', models.FloatField(help_text='*')),
                ('canone_periodicita', models.PositiveSmallIntegerField(help_text='numero mesi *')),
                ('cauzione_importo', models.FloatField(help_text='*')),
                ('cauzione_modalita', models.CharField(help_text='*', max_length=100)),
                ('disdetta_locatore', models.PositiveSmallIntegerField(help_text='numero mesi *')),
                ('disdetta_conduttore', models.PositiveSmallIntegerField(help_text='numero mesi *')),
                ('data_risoluzione', models.DateField(help_text='*')),
                ('modalita_pagamento', models.CharField(help_text='*', max_length=300)),
                ('registrazione_ufficio', models.CharField(help_text='*', max_length=10)),
                ('registrazione_numero', models.CharField(help_text='*', max_length=20)),
                ('registrazione_data', models.DateField(help_text='*')),
            ],
            options={
                'verbose_name': 'contratto di locazione',
                'verbose_name_plural': 'contratti di locazione',
                'ordering': ['conduttore'],
            },
        ),
        migrations.CreateModel(
            name='ContrattoSpesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione', models.TextField(blank=True)),
                ('data', models.DateField(help_text='*')),
                ('importo', models.FloatField(help_text='*')),
                ('percentuale_riaddebito', models.FloatField(blank=True)),
                ('contratto', models.ForeignKey(help_text='*', null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.ContrattoLocazione')),
            ],
            options={
                'verbose_name': 'spesa',
                'verbose_name_plural': 'spese',
                'ordering': ['data'],
            },
        ),
        migrations.CreateModel(
            name='ContrattoTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(help_text='*', max_length=50)),
                ('annualita', models.FloatField(blank=True, verbose_name='attualità')),
            ],
            options={
                'verbose_name': 'tipo di contratto',
                'verbose_name_plural': 'tipi di contratto',
            },
        ),
        migrations.CreateModel(
            name='Immobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sezione', models.CharField(blank=True, max_length=10)),
                ('foglio', models.CharField(blank=True, max_length=10)),
                ('particella_numeratore', models.IntegerField(blank=True)),
                ('particella_denominatore', models.IntegerField(blank=True)),
                ('subalterno', models.CharField(blank=True, max_length=10)),
                ('categoria', models.CharField(help_text='*', max_length=10)),
                ('rendita', models.FloatField(help_text='*')),
                ('condominio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Condominio')),
            ],
            options={
                'verbose_name': 'immobile',
                'verbose_name_plural': 'immobili',
            },
        ),
        migrations.CreateModel(
            name='Indirizzo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toponomia', models.CharField(help_text='*', max_length=100)),
                ('numero_civico', models.PositiveSmallIntegerField(help_text='*')),
                ('comune', models.CharField(help_text='*', max_length=100)),
                ('cap', models.PositiveSmallIntegerField(help_text='*')),
                ('provincia', models.CharField(help_text='*', max_length=100)),
                ('paese', models.CharField(help_text='*', max_length=100)),
            ],
            options={
                'verbose_name': 'indirizzo',
                'verbose_name_plural': 'indirizzi',
                'ordering': ['toponomia'],
            },
        ),
        migrations.CreateModel(
            name='Inquilino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(blank=True, max_length=10)),
                ('nome', models.CharField(help_text='*', max_length=100)),
                ('cognome', models.CharField(help_text='*', max_length=100)),
                ('sesso', models.CharField(choices=[('M', 'Maschio'), ('F', 'Femmina')], help_text='*', max_length=1)),
                ('nascita_data', models.DateField(help_text='*', verbose_name='data di nascita')),
                ('nascita_luogo', models.CharField(help_text='*', max_length=100, verbose_name='luogo di nascita')),
                ('codice_fiscale', models.CharField(help_text='max_length=16 *', max_length=16)),
                ('partita_iva', models.CharField(help_text='*', max_length=20)),
                ('indirizzo', models.ForeignKey(help_text='*', null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Indirizzo')),
            ],
            options={
                'verbose_name': 'inquilino',
                'verbose_name_plural': 'inquilini',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Istat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione', models.TextField(blank=True)),
                ('aliquota', models.FloatField(help_text='*')),
                ('ultima_modifica', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'ISTAT',
                'verbose_name_plural': 'ISTAT',
            },
        ),
        migrations.CreateModel(
            name='Iva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione', models.TextField(blank=True)),
                ('aliquota', models.FloatField(help_text='*')),
                ('ultima_modifica', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'IVA',
                'verbose_name_plural': 'IVA',
            },
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(blank=True, max_length=10)),
                ('nome', models.CharField(help_text='*', max_length=100)),
                ('cognome', models.CharField(help_text='*', max_length=100)),
                ('sesso', models.CharField(choices=[('M', 'Maschio'), ('F', 'Femmina')], help_text='*', max_length=1)),
                ('nascita_data', models.DateField(help_text='*', verbose_name='data di nascita')),
                ('nascita_luogo', models.CharField(help_text='*', max_length=100, verbose_name='luogo di nascita')),
                ('codice_fiscale', models.CharField(help_text='max_length=16 *', max_length=16)),
                ('partita_iva', models.CharField(help_text='*', max_length=20)),
                ('indirizzo', models.ForeignKey(help_text='*', null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Indirizzo')),
            ],
            options={
                'verbose_name': 'proprietario',
                'verbose_name_plural': 'proprietari',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Recapito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_mobile', models.CharField(blank=True, max_length=15)),
                ('numero_fisso', models.CharField(blank=True, max_length=15)),
                ('fax', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('pec', models.EmailField(blank=True, max_length=254, verbose_name='PEC')),
                ('url_sito', models.URLField(blank=True, verbose_name='sito web')),
            ],
            options={
                'verbose_name': 'recapito',
                'verbose_name_plural': 'recapiti',
            },
        ),
        migrations.CreateModel(
            name='Societa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='*', max_length=100)),
                ('tipo', models.CharField(help_text='*', max_length=100)),
                ('codice_fiscale', models.CharField(help_text='max_length=16 *', max_length=16)),
                ('partita_iva', models.CharField(blank=True, max_length=20)),
                ('ufficio', models.CharField(blank=True, max_length=100)),
                ('rea', models.CharField(blank=True, max_length=100)),
                ('costituzione_anno', models.CharField(blank=True, max_length=4)),
                ('capitale_sociale', models.FloatField(blank=True)),
                ('note', models.TextField(blank=True)),
                ('indirizzo', models.ForeignKey(help_text='*', null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Indirizzo')),
                ('recapito', models.ForeignKey(help_text='*', null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Recapito')),
            ],
            options={
                'verbose_name': 'società',
                'verbose_name_plural': 'società',
                'ordering': ['nome'],
            },
        ),
        migrations.AddField(
            model_name='proprietario',
            name='recapito',
            field=models.ForeignKey(help_text='*', null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Recapito'),
        ),
        migrations.AddField(
            model_name='proprietario',
            name='societa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Societa', verbose_name='società'),
        ),
        migrations.AddField(
            model_name='inquilino',
            name='recapito',
            field=models.ForeignKey(help_text='*', null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Recapito'),
        ),
        migrations.AddField(
            model_name='inquilino',
            name='societa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Societa', verbose_name='società'),
        ),
        migrations.AddField(
            model_name='immobile',
            name='indirizzo',
            field=models.ForeignKey(help_text='*', null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Indirizzo'),
        ),
        migrations.AddField(
            model_name='contrattotipo',
            name='istat',
            field=models.ForeignKey(help_text='*', null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Istat'),
        ),
        migrations.AddField(
            model_name='contrattotipo',
            name='iva',
            field=models.ForeignKey(help_text='*', null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Iva'),
        ),
        migrations.AddField(
            model_name='contrattolocazione',
            name='conduttore',
            field=models.ForeignKey(help_text='*', null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Inquilino'),
        ),
        migrations.AddField(
            model_name='contrattolocazione',
            name='contratto_spesa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.ContrattoSpesa'),
        ),
        migrations.AddField(
            model_name='contrattolocazione',
            name='contratto_tipo',
            field=models.ForeignKey(help_text='*', null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.ContrattoTipo'),
        ),
        migrations.AddField(
            model_name='contrattolocazione',
            name='immobile',
            field=models.ForeignKey(help_text='*', null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Immobile'),
        ),
        migrations.AddField(
            model_name='contrattolocazione',
            name='locatore',
            field=models.ForeignKey(help_text='*', null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Proprietario'),
        ),
        migrations.AddField(
            model_name='amministratore',
            name='indirizzo',
            field=models.ForeignKey(help_text='*', null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Indirizzo'),
        ),
        migrations.AddField(
            model_name='amministratore',
            name='recapito',
            field=models.ForeignKey(help_text='*', null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Recapito'),
        ),
        migrations.AddField(
            model_name='amministratore',
            name='societa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='affitti.Societa', verbose_name='società'),
        ),
    ]
