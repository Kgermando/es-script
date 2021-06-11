from django.contrib import admin
import operator
from re import compile
from django.db import models
from django.http import HttpResponse, HttpResponseNotFound, HttpResponse
from django.db.models.query import QuerySet
from django.utils.encoding import smart_str
from datetime import datetime, timedelta
from django import forms
from django.db import models
import string
from random import choice
import csv
import datetime
from django.urls import reverse
from django.utils.safestring import mark_safe

from daterangefilter.filters import PastDateRangeFilter, FutureDateRangeFilter

from issabel.models import Cdr, Cel
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


export_to_csv.short_description = 'Export to CSV'


def cdr_detail(obj):
    return mark_safe('<a href="{}">View</a>'.format(
        reverse('issabel:cdr_issabel_detail', args=[obj.uniqueid]))) 

def cdr_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(
        reverse('issabel:cdr_issabel_detail', args=[obj.uniqueid])))
cdr_pdf.allow_tags = True
cdr_pdf.short_description = 'PDF bill'

class CdrAdmin(admin.ModelAdmin):
    def billsec_norm(obj):
        return timedelta(seconds=obj.billsec)
    billsec_norm.short_description = u'Min.'

    def linksrc(self):
        return u"""<a style='font-size: 12px' href='/admin/issabel/cdr/?accountcode=%s'><b>%s</b></a> <a href='?src=%s'><img style='float: right' src='/media/img/filter.png'></a>""" % (self.accountcode, self.src, self.src)
    linksrc.allow_tags = True
    linksrc.short_description = u'Numéro sortant | Filtre'

    def linkdst(self):
        return u"""%s<a href='?dst=%s'><img style='float: right' src='/media/img/filter.png'></a>""" % (self.dst, self.dst)
    linkdst.allow_tags = True
    linkdst.short_description = u'Numéro sortant | Filtre'

    def linkplay(self):
        if self.recordingfile:
            return mark_safe("<a href='#' onClick=\"set('/sounds/rec/%s', 'Appel de %s, sur: %s', $(this)); return false;\"><img src='/media/img/play.png' alt='Perdre' /></a>" % (self.recordingfile.name, self.src, self.dst))
        else:
            return(u"&nbsp;")
    linkplay.allow_tags = True
    # linkplay.short_description = u''

    list_display = ('calldate', 'dst', 'src', 'dst', 'dcontext', billsec_norm, 'disposition')
    list_filter = (('calldate', PastDateRangeFilter), 'dcontext', )
    search_fields = ('src','dst', 'dcontext')
    actions = [export_to_csv]

    ordering = ['-calldate',]

    def get_actions(self, request):
        """
            Fonction pour Retirer la barre de suppression
        """
        actions = super(CdrAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

class CelAdmin(admin.ModelAdmin):
    list_display = ('uniqueid', 'eventtime', 'amaflags',
                    'context', 'accountcode', 'cid_name', 'exten')
    search_fields = ('uniqueid', 'exten')
    list_display_links = ('uniqueid',)
    list_filter = (('eventtime', PastDateRangeFilter), 'cid_num', 'exten', )
    ordering = ['-eventtime', ]
    read_only_list = ('uniqueid', 'eventtime', 'amaflags',
                      'context', 'accountcode', 'cid_name', 'exten')
    actions = [export_to_csv]

    def get_actions(self, request):
        """
            Retirer la barre de suppression
        """
        actions = super(CelAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions


admin.site.register(Cdr, CdrAdmin)
admin.site.register(Cel, CelAdmin)
