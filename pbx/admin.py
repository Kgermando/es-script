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
    Ps_aors, Ps_auths, Endpoints, Contexts, Extensions,
    IvrDetails, Contacts, AsteriskPublication, Endpoints_id_ips,
    Queue, QueueMember, QueuesConfig, QueueRules, Sip_conf, Sippeers,
    VoiceMail
)

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







class ContextsAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_name', 'incoming',)

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

    # def save_model(self, request, obj, form, change, *args, **kwargs):
    #     if isinstance(obj.password, type(None)):
    #         obj.password = ''
    #     if len(obj.password) == 0:
    #         obj.gen_passwd()
    #     obj.payer = obj.mailbox.accountcode
    #     obj.save()


class QueueAdmin(admin.ModelAdmin):
    list_display = ('id', 'context', 'musiconhold', 'name',)


admin.site.register(Ps_aors)
admin.site.register(Ps_auths)
admin.site.register(Endpoints, EndpointsAdmin)
admin.site.register(Contexts, ContextsAdmin)
admin.site.register(Extensions, ExtensionsAdmin)
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
