from django.contrib import admin
import operator
from re import compile
from django.db import models
from django.http import HttpResponse, HttpResponse
from datetime import datetime, timedelta
import csv
from daterangefilter.filters import PastDateRangeFilter, FutureDateRangeFilter

from contacts.models import Contact
# Register your models here.

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;' \
                                      'filename={}.csv'.format(
                                          opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields(
    ) if not field.many_to_many and not field.one_to_many]
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


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'Nom', 'Post_Nom', 'Prenom', 'Numero', 'Rue', 'Quartier', 'Commune', 'Ville',
        'Province', 'Tel1', 'Tel2', 'Email', 'Website', 'Facebook', 'Instagram',
        'Twitter', 'LinkedIn', 'Remarque', 'created_date', 'user'
    )

    search_fields = (
        'Nom', 'Post_Nom', 'Prenom', 'Tel1', 'Tel2', 'Email', 'Province',
    )

    list_filter = (
        ('created_date', PastDateRangeFilter),
        'Province',
    )



    actions = [export_to_csv]

    ordering = ['-created_date', ]
