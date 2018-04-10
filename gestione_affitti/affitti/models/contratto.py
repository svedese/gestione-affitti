from django.db import models
from .dettagli import Indirizzo, Istat, Iva
from .models import Proprietario, Inquilino, Amministratore


# Create your models here.

class ContrattoLocazione(models.Model):
    locatore = models.ForeignKey(Proprietario, on_delete=models.SET_NULL, null=True, help_text='')
    conduttore = models.ForeignKey(Inquilino, on_delete=models.SET_NULL, null=True, help_text='')
    # immobile = models.ForeignKey(Immobile, on_delete=models.SET_NULL, null=True, help_text='')
    contratto_tipo = models.ForeignKey('ContrattoTipo', on_delete=models.SET_NULL, null=True, help_text='')
    # contratto_spesa = models.ForeignKey('ContrattoSpesa', on_delete=models.SET_NULL, null=True, blank=True)
    decorrenza = models.PositiveSmallIntegerField(help_text='numero mesi')
    durata = models.PositiveSmallIntegerField(help_text='numero mesi')  # models.DateField
    data_stipula = models.DateField(help_text='')
    canone_importo = models.FloatField(help_text='')
    canone_periodicita = models.PositiveSmallIntegerField(help_text='numero mesi ')
    cauzione_importo = models.FloatField(help_text='')
    cauzione_modalita = models.CharField(max_length=100, help_text='')  # models.CharField(choices)
    disdetta_locatore = models.PositiveSmallIntegerField(help_text='numero mesi')
    disdetta_conduttore = models.PositiveSmallIntegerField(help_text='numero mesi')
    data_risoluzione = models.DateField(help_text='')
    modalita_pagamento = models.CharField(max_length=300, help_text='')
    registrazione_ufficio = models.CharField(max_length=10, help_text='')
    registrazione_numero = models.CharField(max_length=20, help_text='')
    registrazione_data = models.DateField(help_text='')

    def __str__(self):
        return '%s %s' % (self.conduttore.cognome, self.conduttore.nome)

    class Meta:
        ordering = ['conduttore']
        verbose_name = 'contratto di locazione'
        verbose_name_plural = 'contratti di locazione'


class ContrattoSpesa(models.Model):
    contratto = models.ForeignKey('ContrattoLocazione', on_delete=models.SET_NULL, null=True, help_text='')
    descrizione = models.TextField(blank=True)
    data = models.DateField(help_text='')
    importo = models.FloatField(help_text='')
    percentuale_riaddebito = models.FloatField(blank=True)

    def __str__(self):
        return '%f %s' % (self.importo, self.data)

    class Meta:
        ordering = ['data']
        verbose_name = 'spesa'
        verbose_name_plural = 'spese'


class ContrattoTipo(models.Model):
    tipo = models.CharField(max_length=50, help_text='')
    istat = models.ForeignKey(Istat, on_delete=models.SET_NULL, null=True, help_text='')
    iva = models.ForeignKey(Iva, on_delete=models.SET_NULL, null=True, help_text='')
    annualita = models.FloatField(verbose_name='attualità', blank=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'tipo di contratto'
        verbose_name_plural = 'tipi di contratto'


class Immobile(models.Model):
    codice_catastale = models.CharField(max_length=10, blank=True)
    sezione = models.CharField(max_length=10, blank=True)
    foglio = models.CharField(max_length=10, blank=True)
    particella_numeratore = models.IntegerField(blank=True)
    particella_denominatore = models.IntegerField(blank=True)
    subalterno = models.CharField(max_length=10, blank=True)
    categoria = models.CharField(max_length=10, help_text='')
    rendita = models.FloatField(help_text='')
    indirizzo = models.ForeignKey(Indirizzo, on_delete=models.SET_NULL, null=True, help_text='')
    # condominio = models.ForeignKey('Condominio', on_delete=models.SET_NULL, null=True, blank=True)
    contratto = models.ForeignKey('ContrattoLocazione', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'immobile'
        verbose_name_plural = 'immobili'


class Condominio(models.Model):
    nome = models.CharField(max_length=100, help_text='*')
    immobile = models.ForeignKey(Immobile, on_delete=models.SET_NULL, null=True, blank=True)
    codice_fiscale = models.CharField(max_length=16, help_text='max_length=16')
    amministratore = models.ForeignKey(Amministratore, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'condominio'
        verbose_name_plural = 'condomini'
