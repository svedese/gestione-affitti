from django.db import models
from .dettagli import Indirizzo, Recapito


# Create your models here.

class PersonaFisica(models.Model):
    SESSO_CHOICES = (
        ('M', 'Maschio'),
        ('F', 'Femmina'),
    )

    titolo = models.CharField(max_length=10, blank=True)
    nome = models.CharField(max_length=100, help_text='')
    cognome = models.CharField(max_length=100, primary_key=True, help_text='')
    sesso = models.CharField(max_length=1, choices=SESSO_CHOICES, help_text='')
    nascita_data = models.DateField(verbose_name='data di nascita', help_text='')
    nascita_luogo = models.CharField(max_length=100, verbose_name='luogo di nascita', help_text='')
    codice_fiscale = models.CharField(max_length=16, help_text='max_length=16')
    # partita_iva = models.CharField(max_length=20, help_text='')
    indirizzo = models.ForeignKey(Indirizzo, on_delete=models.SET_NULL, null=True, help_text='')
    recapito = models.ForeignKey(Recapito, on_delete=models.SET_NULL, null=True, help_text='')

    def __str__(self):
        return '%s %s' % (self.cognome, self.nome)

    class Meta:
        abstract = True
        verbose_name = 'persona fisica'
        verbose_name_plural = 'persone fisiche'


class PersonaGiuridica(models.Model):
    nome = models.CharField(max_length=100, primary_key=True, help_text='')
    tipo = models.CharField(max_length=100, help_text='')
    codice_fiscale = models.CharField(max_length=16, help_text='max_length=16')
    partita_iva = models.CharField(max_length=11, blank=True)
    ufficio = models.CharField(max_length=100, blank=True)
    rea = models.CharField(max_length=100, blank=True)
    costituzione_anno = models.CharField(max_length=4, blank=True)
    capitale_sociale = models.FloatField(blank=True)
    note = models.TextField(blank=True)
    indirizzo = models.ForeignKey(Indirizzo, on_delete=models.SET_NULL, null=True, help_text='')
    recapito = models.ForeignKey(Recapito, on_delete=models.SET_NULL, null=True, help_text='')

    def __str__(self):
        return self.nome

    class Meta:
        abstract = True
        verbose_name = 'persona giuridica'
        verbose_name_plural = 'persone giuridiche'
