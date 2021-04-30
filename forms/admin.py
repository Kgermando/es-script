from django.contrib import admin
import operator
from re import compile
from django.db import models
from django.http import HttpResponse, HttpResponseNotFound, HttpResponse
from django.db.models.query import QuerySet
from django.utils.encoding import smart_str
from datetime import datetime, timedelta
import csv
import datetime

from daterangefilter.filters import PastDateRangeFilter, FutureDateRangeFilter

from forms.models import Kyc, Contact
# Register your models here.
def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;' \
                                      'filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


@admin.register(Kyc)
class scriptAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'questions1', 'questions2', 'questions3', 'questions4', 'questions5', 'questions6', 'questions7', 'questions8', 'questions9',
        'questions10', 'questions12', 'questions13', 'questions15', 'questions16', 'Q19temps_a_contacter',
        'montant_de_pret', 'duree_de_credit', 'montant_a_rembourser_chaque_mois', 'montant_des_ventes_bonne_journee',
        'montant_des_ventes_mauvaise_journee', 'date_a_laquelle_recevoir_credit', 'Nom_du_garant', 'Activite',
        'Remarque', 'Commentaire', 'Concurrent', 'CommentaireQ17',
        'Nom_societe', 'Nom', 'Post_Nom', 'Prenom', 'Numero', 'Quartier', 'Commune', 'Province',
        'Pays', 'Tel1', 'Tel2', 'Email', 'Website', 'Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'Statut',
    )
    list_filter = (
        # 'Nom_societe', 'Nom', 'Post_Nom', 'Prenom',
        ('created_date', PastDateRangeFilter), 
    )
    actions = [export_to_csv]

    ordering = ['-created_date', ]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'Nom', 'Post_Nom', 'Prenom', 'Numero', 'Quartier', 'Commune', 'Province', 
        'Pays', 'Tel1', 'Tel2', 'Email', 'Website', 'Facebook', 'Instagram', 
        'Twitter', 'LinkedIn', 'Remarque', 'created_date'
    )

    list_filter = (
        ('created_date', PastDateRangeFilter),
    )

    actions = [export_to_csv]

    ordering = ['-created_date', ]
