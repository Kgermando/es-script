from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Cdr(models.Model):
    calldate        = models.DateTimeField()
    clid            = models.CharField(max_length=80, null=False, blank=True)
    src             = models.CharField(max_length=80, null=False, blank=True)
    dst             = models.CharField(max_length=80, null=False, blank=True)
    dcontext        = models.CharField(max_length=80, null=False, blank=True)
    channel         = models.CharField(max_length=80, null=False, blank=True)
    dstchannel      = models.CharField(max_length=80, null=False, blank=True)
    lastapp         = models.CharField(max_length=80, null=False, blank=True)
    lastdata        = models.CharField(max_length=80, null=False, blank=True)
    duration        = models.IntegerField(default=0, null=False, blank=True)
    billsec         = models.IntegerField(default=0, null=False, blank=True)
    disposition     = models.CharField(max_length=45, editable=True, default='', null=False, db_index=True)
    amaflags        = models.PositiveIntegerField(editable=True, default=0, null=False, db_index=True)
    accountcode     = models.CharField(max_length=20, null=False, blank=True)
    uniqueid        = models.AutoField(auto_created=True, primary_key=True, serialize=False, editable=True, verbose_name='Unique ID')
    userfield       = models.CharField(max_length=255, null=False, blank=True)
    recordingfile   = models.CharField(max_length=255, null=False, blank=True)
    cnum            = models.CharField(max_length=80, null=False, blank=True)
    cnam            = models.CharField(max_length=80, null=False, blank=True)
    outbound_cnum   = models.CharField(max_length=80, null=False, blank=True)
    outbound_cnam   = models.CharField(max_length=80, null=False, blank=True)
    dst_cnam        = models.CharField(max_length=80, null=False, blank=True)
    did             = models.CharField(max_length=50, null=False, blank=True)

    class Meta:
        db_table = 'cdr'
    
    def billsec_norm(obj):
        return timedelta(seconds=obj.billsec)
    billsec_norm.short_description = u'Min.'

    def duration_cout(self):
        return self.duration * 2.08
    
    def duration_cout_total(self):
        return sum(item.duration_cout() for item in self.items.all())


class Cel(models.Model):
    """
       SQL CREATE TABLE cel
    """
    eventtime = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    eventtype = models.CharField(max_length=80, default='', blank=True, null=False)
    userdeftype = models.CharField(max_length=80, default='', blank=True, null=False)
    cid_name = models.CharField(max_length=80, default='', blank=True, null=False)
    cid_num = models.CharField(max_length=80, default='', blank=True, null=False)
    cid_ani = models.CharField(max_length=80, default='', blank=True, null=False)
    cid_rdnis = models.CharField(max_length=80, default='', blank=True, null=False)
    cid_dnid = models.CharField(max_length=80, default='', blank=True, null=False)
    exten = models.CharField(max_length=80, default='', blank=True, null=False)
    context = models.CharField(max_length=80, default='', blank=True, null=False)
    channame = models.CharField(max_length=80, default='', blank=True, null=False)
    appname = models.CharField(max_length=80, default='', blank=True, null=False)
    appdata = models.CharField(max_length=80, default='', blank=True, null=False)
    amaflags = models.IntegerField(default=0, blank=True, null=False)
    accountcode = models.CharField(max_length=20, default='', blank=True, null=False)
    uniqueid = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Unique ID')
    linkedid = models.CharField(max_length=80, default='', blank=True, null=False)
    peer = models.CharField(max_length=80, default='', blank=True, null=False)
    userdeftype = models.CharField(max_length=255, default='', blank=True, null=False)
    eventextra = models.CharField(max_length=255, default='', blank=True, null=False)
    userfield = models.CharField(max_length=255, default='', blank=True, null=False)


    def __unicode__(self, *args, **kwargs):
        return u'%s | %s --> %s длит.: %s сек.' % (self.eventtime, self.context, self.exten, self.amaflags)


    class Meta:
        db_table = 'cel'
