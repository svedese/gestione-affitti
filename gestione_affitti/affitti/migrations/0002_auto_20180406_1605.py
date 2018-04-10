# Generated by Django 2.0.3 on 2018-04-06 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affitti', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amministratore',
            name='id',
        ),
        migrations.RemoveField(
            model_name='inquilino',
            name='id',
        ),
        migrations.RemoveField(
            model_name='proprietario',
            name='id',
        ),
        migrations.RemoveField(
            model_name='societa',
            name='id',
        ),
        migrations.AddField(
            model_name='immobile',
            name='codice_catastale',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='amministratore',
            name='cognome',
            field=models.CharField(help_text='*', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inquilino',
            name='cognome',
            field=models.CharField(help_text='*', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='cognome',
            field=models.CharField(help_text='*', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='societa',
            name='nome',
            field=models.CharField(help_text='*', max_length=100, primary_key=True, serialize=False),
        ),
    ]
