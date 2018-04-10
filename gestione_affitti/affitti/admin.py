from django.contrib import admin
from .models import ContrattoLocazione, ContrattoSpesa, Immobile, Condominio, Proprietario, Inquilino, Amministratore
from django.forms import Textarea, TextInput
from django.db import models

# Register your models here.

class CondominioInline(admin.TabularInline):
    model = Condominio
    extra = 1


class ImmobileInline(admin.TabularInline):
    model = Immobile
    extra = 1
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})}
    }


class ContrattoSpesaInline(admin.TabularInline):
    model = ContrattoSpesa
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 50})}
    }


class ImmobileAdmin(admin.ModelAdmin):
    list_display = ('indirizzo', 'categoria')
    inlines = [CondominioInline]


class ProprietarioAdmin(admin.ModelAdmin):
    list_display = ('cognome', 'nome', 'indirizzo')


class InquilinoAdmin(admin.ModelAdmin):
    list_display = ('cognome', 'nome', 'indirizzo')


class AmministratoreAdmin(admin.ModelAdmin):
    list_display = ('cognome', 'nome', 'indirizzo')


class ContrattoLocazioneAdmin(admin.ModelAdmin):
    list_display = ('locatore', 'conduttore', 'data_risoluzione')
    fields = [('locatore', 'conduttore'),
              'contratto_tipo',
              ('decorrenza', 'durata'),
              ('data_stipula', 'data_risoluzione'),
              ('canone_importo', 'canone_periodicita'),
              ('cauzione_importo', 'cauzione_modalita'),
              ('disdetta_locatore', 'disdetta_conduttore'),
              'modalita_pagamento',
              'registrazione_ufficio',
              'registrazione_numero',
              'registrazione_data',
              ]
    inlines = [
        ImmobileInline,
        ContrattoSpesaInline,
    ]


admin.site.register(ContrattoLocazione, ContrattoLocazioneAdmin)
admin.site.register(Immobile, ImmobileAdmin)
admin.site.register(Condominio)
admin.site.register(Proprietario, ProprietarioAdmin)
admin.site.register(Inquilino, InquilinoAdmin)
admin.site.register(Amministratore, AmministratoreAdmin)
