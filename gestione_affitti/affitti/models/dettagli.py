from django.db import models


# Create your models here.

class Indirizzo(models.Model):
    nome = models.CharField(max_length=15, blank=True)
    toponomia = models.CharField(max_length=100, help_text='')
    numero_civico = models.PositiveSmallIntegerField(help_text='')
    comune = models.CharField(max_length=100, help_text='')
    cap = models.PositiveSmallIntegerField(help_text='')
    provincia = models.CharField(max_length=100, help_text='')
    paese = models.CharField(max_length=100, help_text='')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['toponomia']
        verbose_name = 'indirizzo'
        verbose_name_plural = 'indirizzi'


class Recapito(models.Model):
    nome = models.CharField(max_length=15, blank=True)
    numero_mobile = models.CharField(max_length=25, blank=True)
    numero_fisso = models.CharField(max_length=25, blank=True)
    fax = models.CharField(max_length=25, blank=True)
    email = models.EmailField(verbose_name='email', blank=True)
    pec = models.EmailField(verbose_name='PEC', blank=True)
    url_sito = models.URLField(verbose_name='sito web', blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'recapito'
        verbose_name_plural = 'recapiti'


class Iva(models.Model):
    descrizione = models.TextField(blank=True)
    aliquota = models.FloatField(help_text='')
    ultima_modifica = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ultima_modifica

    class Meta:
        verbose_name = 'IVA'
        verbose_name_plural = 'IVA'


class Istat(models.Model):
    descrizione = models.TextField(blank=True)
    aliquota = models.FloatField(help_text='')
    ultima_modifica = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ultima_modifica

    class Meta:
        verbose_name = 'ISTAT'
        verbose_name_plural = 'ISTAT'
