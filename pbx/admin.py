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

from pbx.models import (
    Ps_aors, Ps_auths, Endpoints, Contexts, Extensions, Cdr, Cel,
    IvrDetails, Contacts, AsteriskPublication, Endpoints_id_ips,
    Queue, QueueMember, QueuesConfig, QueueRules, Sip_conf, Sippeers,
    VoiceMail
)

# Register your models here.
def cdr_detail(obj):
    return mark_safe('<a href="{}">View</a>'.format(
        reverse('pbx:cdr_detail', args=[obj.uniqueid])))

def cdr_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(
        reverse('pbx:cdr_detail', args=[obj.uniqueid])))
cdr_pdf.allow_tags = True
cdr_pdf.short_description = 'PDF bill'


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







class ContextsAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_name', 'incoming',)

class CdrAdmin(admin.ModelAdmin):
    def billsec_norm(obj):
        return timedelta(seconds=obj.billsec)
    billsec_norm.short_description = u'Min.'

    def linksrc(self):
        return u"""<a style='font-size: 12px' href='/admin/pbx/cdr/?accountcode=%s'><b>%s</b></a> <a href='?src=%s'><img style='float: right' src='/media/img/filter.png'></a>""" % (self.accountcode, self.src, self.src)
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

    list_display = ('calldate', linkplay, linksrc, linkdst, 'dcontext', billsec_norm, 'disposition', cdr_detail,)
    list_filter = ('dcontext', 'disposition', 'amaflags', 'calldate',)
    search_fields = ('src','dst',)
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
    ordering = ['-eventtime', ]
    read_only_list = ('uniqueid', 'eventtime', 'amaflags',
                      'context', 'accountcode', 'cid_name', 'exten')

    def get_actions(self, request):
        """
            Retirer la barre de suppression
        """
        actions = super(CelAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions


class ExtensionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'context', 'exten', 'priority', 'app', 'appdata', )
    ordering = ['context__name', 'exten', 'priority', ]
    search_fields = ('=app', 'appdata')
    list_filter = ('context', 'exten')
    # list_editable = ('context', 'exten','priority', 'app', 'appdata', )
    list_display_links = ('id',)


class Sip_confAdmin(admin.ModelAdmin):
    list_display = ('name', 'secret', 'callerid', 'context', 'host', 'ipaddr')
    list_filter = ('context', 'amaflags', 'dtmfmode')
    search_fields = ('name',)
    ordering = ['name',]
    radio_fields = {"dtmfmode": admin.VERTICAL, "insecure": admin.VERTICAL, "type": admin.VERTICAL, "amaflags": admin.VERTICAL,  }

    def get_readonly_fields(self, request, obj=None):
        fields = super(Sip_confAdmin, self).get_readonly_fields(request, obj)
        if not request.user.is_superuser:
            return ('host','nat','type','amaflags','callgroup','callerid',
                    'cancallforward','directmedia','defaultip','dtmfmode', 'port',
                    'insecure','language','mailbox','musiconhold','pickupgroup', 'directmedia',
                    'qualify','disallow','allow','trustrpid','sendrpid','videosupport')
        return fields

    def get_actions(self, request):
        actions = super(Sip_confAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions


class EndpointsAdmin(admin.ModelAdmin):
    list_display = ('id', 'context', 'aors', 'auth', 'mailboxes', 'transport', )
    ordering = ['id', 'context', 'aors', 'auth', 'mailboxes', 'transport',]
    search_fields = ('=id', 'context')
    list_filter = ('context', 'id')
    list_editable = ('context', 'aors', 'auth', 'mailboxes', 'transport',)
    list_display_links = ('id',)



class VoicemailAdmin(admin.ModelAdmin):
    list_display = ('mailbox', 'password', 'stamp')
    search_fields = ('mailbox',)
    ordering = ['mailbox', ]
    list_display_links = ('mailbox',)

    def save_model(self, request, obj, form, change, *args, **kwargs):
        if isinstance(obj.password, type(None)):
            obj.password = ''
        if len(obj.password) == 0:
            obj.gen_passwd()
        obj.payer = obj.mailbox.accountcode
        obj.save()


class QueueAdmin(admin.ModelAdmin):
    list_display = ('id', 'context', 'musiconhold', 'name',)


admin.site.register(Ps_aors)
admin.site.register(Ps_auths)
admin.site.register(Endpoints, EndpointsAdmin)
admin.site.register(Contexts, ContextsAdmin)
admin.site.register(Extensions, ExtensionsAdmin)
admin.site.register(Cdr, CdrAdmin)
admin.site.register(Cel, CelAdmin)
admin.site.register(IvrDetails)
admin.site.register(Contacts)
admin.site.register(AsteriskPublication)
admin.site.register(Endpoints_id_ips)
admin.site.register(Queue, QueueAdmin)
admin.site.register(QueueMember)
admin.site.register(QueuesConfig)
admin.site.register(QueueRules)
admin.site.register(Sip_conf, Sip_confAdmin)
admin.site.register(Sippeers)
admin.site.register(VoiceMail, VoicemailAdmin)
