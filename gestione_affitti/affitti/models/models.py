from django.db import models
from .anagrafica import PersonaFisica, PersonaGiuridica
from .dettagli import Indirizzo


# Create your models here.
"""
class Immobile(models.Model):
    codice_catastale = models.CharField(max_length=10, blank=True)
    sezione = models.CharField(max_length=10, blank=True)
    foglio = models.CharField(max_length=10, blank=True)
    particella_numeratore = models.IntegerField(blank=True)
    particella_denominatore = models.IntegerField(blank=True)
    subalterno = models.CharField(max_length=10, blank=True)
    categoria = models.CharField(max_length=10, help_text='*')
    rendita = models.FloatField(help_text='*')
    indirizzo = models.ForeignKey(Indirizzo, on_delete=models.SET_NULL, null=True, help_text='*')
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
    codice_fiscale = models.CharField(max_length=16, help_text='max_length=16 *')
    amministratore = models.ForeignKey('Amministratore', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'condominio'
        verbose_name_plural = 'condomini'
"""

class Proprietario(PersonaFisica):
    societa = models.ForeignKey('Societa',
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                verbose_name='società')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'proprietario'
        verbose_name_plural = 'proprietari'


class Inquilino(PersonaFisica):
    societa = models.ForeignKey('Societa',
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                verbose_name='società')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'inquilino'
        verbose_name_plural = 'inquilini'


class Amministratore(PersonaFisica):
    societa = models.ForeignKey('Societa',
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                verbose_name='società')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'amministratore'
        verbose_name_plural = 'amministratori'


class Societa(PersonaGiuridica):

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'società'
        verbose_name_plural = 'società'
