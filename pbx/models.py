from django.db import models
from datetime import time, datetime
from random import randint, choice
from datetime import datetime, timedelta

from pbx.extensionsApps import APPS, MUSICONHOLD
# Create your models here.
ranged = [(i,i) for i in range(11)]
rangedAMAFLAGS = [(i,i) for i in range(6)]
MAX_CONTACTS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10), 
)
AMAFLAGS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10), 
)

Q_FREQUENCE = (
    (30, 30),
    (40, 40),
    (50, 50),
    (60, 60),
)
YES_NO = (
    ('yes', 'yes'),
    ('no', 'no'),
)
TRANSPORT = (
    ('transport-udp', 'transport-udp'),
    ('transport-tcp', 'transport-tcp'),
)
TRANSPORT_SIP = (
    ('udp','udp'),
    ('tcp','tcp'),
    ('udp,tcp','udp,tcp'),
    ('tcp,udp','tcp,udp'),
)


ALLOW = (
    ('all', 'all'),
    ('alaw', 'alaw'),
    ('disallow', 'disallow'),
)
IN_OUT = (
    (True, 'Entrant'),
    (False, 'Sortant'),
)
QUEUE_AUTOPAUSE = (
    ('queue', 'queue'),
    ('autopause', 'autopause'),
)

QUEUE_STRATEGY = (
    ('queue', 'queue'),
    ('strategy', 'strategy'),
)

DISPOSITIONS=(
    ('ANSWERED','ANSWERED'),
    ('FAILED', 'FAILED'),
    ('NO ANSWER','NO ANSWER'),
    ('BUSY','BUSY'),
    ('DOCUMENTATION','DOCUMENTATION'),
    ('BILL','BILL'),
    ('IGNORE','IGNORE'),
)
TYPE_SIP = (
    ('friend', 'friend'),
    ('peer', 'peer'),
    ('user', 'user'),
)

INSECURE_SIP = (
    ('port', 'port'),
    ('very', 'very'),
    ('no', 'no'),
)

DTMFMODE_SIP = (
    ('rfc2833', 'rfc2833'),
    ('info', 'info'),
    ('shortinfo', 'shortinfo'),
    ('inband', 'inband'),
    ('auto', 'auto'),
)

TRUEFALSE = (
    (False, False),
    (True, True)
)

DIRECTMEDIA = (
    ('yes', 'yes'),
    ('no', 'no'),
    ('nonat', 'nonat'),
    ('update', 'update'),
)


INVITE = (
    ('port', "Ignorez le numéro de port d'où provient l'authentification"),
    ('invite', "Ne nécessite pas d'INVITATION initiale pour l'authentification"),
    ('port,invite', "N'exigez pas l'INVITE initiale pour l'authentification et ignorez le port d'où provient la demande"),
)

NAT = (
    ('yes', 'yes'),
    ('no', 'no'),
    ('never', 'never'),
    ('route', 'route'),
)

CALLINGPRES = (
    ('allowed_not_screened', 'allowed_not_screened'),
    ('allowed_passed_screen', 'allowed_passed_screen'),
    ('allowed_failed_screen', 'allowed_failed_screen'),
    ('allowed', 'allowed'),
    ('prohib_not_screened', 'prohib_not_screened'),
    ('prohib_passed_screen', 'prohib_passed_screen'),
    ('prohib_failed_screen', 'prohib_failed_screen'),
    ('prohib', 'prohib'),
)

PROGRESSINBAND = (
    ('yes', 'yes'),
    ('no', 'no'),
    ('never', 'never'),
)

SESSIONTIMERS = (
    ('accept', 'accept'),
    ('refuse', 'refuse'),
    ('originate', 'originate'),
)

SESSIONREFRESHER = (
    ('uac', 'uac'),
    ('uas', 'uas'),
)



class Contexts(models.Model):
    """
        Context for extensions
    """
    name = models.CharField(max_length=25, primary_key=True,  blank=False, null=False, verbose_name='le contexte', editable=True)
    full_name = models.CharField(max_length=25, blank=False, null=False, verbose_name='la description', editable=True)
    incoming = models.BooleanField(default=False, null=False, blank=False, verbose_name='Entrant', choices=IN_OUT, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Context'
        verbose_name_plural = u'Contexts'
        db_table = 'contexts'

class Ps_aors(models.Model):
    id                  = models.BigIntegerField(unique=True, primary_key=True, serialize=False, verbose_name='Unique ID', editable=True)
    max_contacts        = models.PositiveIntegerField(u'max_contacts', choices=MAX_CONTACTS)
    qualify_frequency   = models.PositiveIntegerField(u'Qualites de Frequence', choices=Q_FREQUENCE)
    contact             = models.CharField(max_length=255, null=True, blank=True, db_column='contact')
    default_expiration  = models.PositiveIntegerField(null=True, blank=True)
    minimum_expiration  = models.PositiveIntegerField(null=True, blank=True)
    remove_existing     = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    authenticate_qualify = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    maximum_expiration  = models.PositiveIntegerField(null=True, blank=True)
    outbound_proxy      = models.CharField(max_length=40, null=True, blank=True)
    support_path        = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    qualify_timeout     = models.FloatField(null=True, blank=True)
    voicemail_extension = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = u'Ps_aor'
        verbose_name_plural = u'Ps_aors'
        db_table = 'ps_aors'


class Ps_auths(models.Model):
    '''
        Module auth
    '''
    id             = models.BigIntegerField(unique=True, primary_key=True, serialize=False, verbose_name='Unique ID', editable=True)
    auth_type      = models.CharField(max_length=200, null=True, blank=True, default='userpass')
    nonce_lifetime = models.PositiveIntegerField(blank=True, null=True)
    md5_cred       = models.CharField(max_length=40, blank=True, null=True)
    password       = models.CharField(max_length=80)
    realm          = models.CharField(max_length=40, blank=True, null=True)
    username       = models.CharField(max_length=40, help_text='101')
    refresh_token  = models.CharField(max_length=255, blank=True, null=True)
    oauth_clientid = models.CharField(max_length=255, blank=True, null=True)
    oauth_secret   = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "%s" %(self.username)

    class Meta:
        verbose_name = u'Ps_auth'
        verbose_name_plural = u'Ps_auths'
        db_table = 'ps_auths'


class Extensions(models.Model):
    '''
        Module de gestions d'appels
    '''
    context = models.ForeignKey(Contexts, on_delete=models.CASCADE, max_length=40, blank=True, null=True, db_column='context', db_index=True)
    exten = models.CharField(max_length=40, blank=True, null=True, help_text='exten / template', db_index=True)
    priority = models.IntegerField(null=True, blank=True, help_text='priorité')
    app = models.CharField(max_length=40, choices=APPS, blank=True, null=True, help_text='application de plan de numérotation', db_index=True)
    appdata = models.CharField(max_length=256, blank=True, null=True, help_text='paramètres d\'application', db_index=True)

    def __str__(self):
        return self.exten

    class Meta:
        verbose_name = u'Extension'
        verbose_name_plural = u'Extensions'
        db_table = 'extensions'


class Endpoints(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True, serialize=False, verbose_name='Unique ID', editable=True)
    transport = models.CharField(u'transport', max_length=40, choices=TRANSPORT, null=True)
    aors = models.PositiveIntegerField(unique=True, help_text='101', db_column='aors')
    auth = models.PositiveIntegerField(unique=True, help_text='101', db_column='auth')
    context = models.ForeignKey(Contexts, on_delete=models.CASCADE, max_length=200, db_column='context')
    disallow = models.CharField(max_length=200, null=True, blank=True, default='all', choices=ALLOW)
    allow = models.CharField(max_length=200, null=True, blank=True, default='all', choices=ALLOW)
    direct_media = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    deny = models.CharField(max_length=95, blank=True, null=True, default='0.0.0.0/0', verbose_name='sous-réseaux interdits')
    permit = models.CharField(max_length=95, blank=True, null=True, default='0.0.0.0/0', verbose_name='sous-réseaux autorisés')
    mailboxes = models.CharField(max_length=40, null=True, help_text='100@default')
    connected_line_method = models.CharField(max_length=100, null=True, blank=True, help_text='pjsip_connected_line_method_values')
    direct_media_method = models.CharField(max_length=100, null=True, blank=True, help_text='pjsip_connected_line_method_values')
    direct_media_glare_mitigation = models.CharField(max_length=100, null=True, blank=True, help_text='pjsip_direct_media_glare_mitigation_values')
    disable_direct_media_on_nat = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    dtmf_mode = models.CharField(max_length=100, null=True, blank=True, help_text='pjsip_dtmf_mode_values_v3')
    external_media_address = models.CharField(max_length=40, blank=True, null=True)
    force_rport = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    ice_support = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    identify_by = models.CharField(max_length=40, null=True, blank=True)
    moh_suggest  = models.CharField(max_length=40, null=True, blank=True)
    outbound_auth = models.CharField(max_length=40, null=True, blank=True)
    outbound_proxy = models.CharField(max_length=40, null=True, blank=True)
    rewrite_contact = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    rtp_ipv6 = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    rtp_symmetric = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    send_diversion = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    send_pai = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    send_rpid = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    timers_min_se = models.PositiveIntegerField(null=True, blank=True)
    timers = models.CharField(max_length=100, null=True, blank=True, help_text='pjsip_timer_values')
    timers_sess_expires = models.PositiveIntegerField(null=True, blank=True)
    callerid = models.CharField(max_length=40, null=True, blank=True)
    callerid_privacy = models.CharField(max_length=100, null=True, blank=True, help_text='pjsip_cid_privacy_values')
    callerid_tag = models.CharField(max_length=40, null=True, blank=True)
    r100rel = models.CharField(max_length=100, null=True, blank=True, db_column='100rel', help_text='pjsip_100rel_values')
    aggregate_mwi = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    trust_id_inbound = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    trust_id_outbound = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    use_ptime = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    use_avpf = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    media_encryption = models.CharField(max_length=100, null=True, blank=True, help_text='pjsip_media_encryption_values')
    inband_progress = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    call_group = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    pickup_group = models.CharField(max_length=40, null=True, blank=True)
    named_call_group = models.CharField(max_length=40, null=True, blank=True)
    named_pickup_group = models.CharField(max_length=40, null=True, blank=True)
    device_state_busy_at = models.PositiveIntegerField(null=True, blank=True)
    fax_detect = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    t38_udptl = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    t38_udptl_ec  = models.CharField(max_length=100, null=True, blank=True, help_text='pjsip_t38udptl_ec_values')
    t38_udptl_maxdatagram = models.PositiveIntegerField(null=True, blank=True)
    t38_udptl_nat = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    t38_udptl_ipv6 = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    tone_zone = models.CharField(max_length=40, null=True, blank=True)
    language = models.CharField(max_length=40, null=True, blank=True)
    one_touch_recording = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    record_on_feature = models.CharField(max_length=40, null=True, blank=True)
    record_off_feature = models.CharField(max_length=40, null=True, blank=True)
    rtp_engine = models.CharField(max_length=40, null=True, blank=True)
    allow_transfer = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    allow_subscribe = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    sdp_owner = models.CharField(max_length=40, null=True, blank=True)
    sdp_session = models.CharField(max_length=40, null=True, blank=True)
    tos_audio = models.CharField(max_length=10, null=True, blank=True)
    tos_video = models.CharField(max_length=10, null=True, blank=True)
    sub_min_expiry = models.PositiveIntegerField(null=True, blank=True)
    from_domain = models.CharField(max_length=40, null=True, blank=True)
    from_user = models.CharField(max_length=40, null=True, blank=True)
    mwi_from_user = models.CharField(max_length=40, null=True, blank=True)
    dtls_verify = models.CharField(max_length=40, null=True, blank=True)
    dtls_rekey = models.CharField(max_length=40, null=True, blank=True)
    dtls_cert_file = models.CharField(max_length=200, null=True, blank=True)
    dtls_private_key = models.CharField(max_length=200, null=True, blank=True)
    dtls_cipher = models.CharField(max_length=200, null=True, blank=True)
    dtls_ca_file = models.CharField(max_length=200, null=True, blank=True)
    dtls_ca_path = models.CharField(max_length=200, null=True, blank=True)
    dtls_setup = models.CharField(max_length=200, null=True, blank=True, help_text='pjsip_dtls_setup_values')
    srtp_tag_32 = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    media_address = models.CharField(max_length=40, null=True, blank=True)
    redirect_method = models.CharField(max_length=200, null=True, blank=True, help_text='pjsip_redirect_method_values')
    set_var = models.TextField(null=True, blank=True)
    cos_audio = models.PositiveIntegerField(null=True, blank=True)
    cos_video = models.PositiveIntegerField(null=True, blank=True)
    message_context = models.CharField(max_length=40, null=True, blank=True)
    force_avp = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    media_use_received_transport = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    accountcode = models.CharField(max_length=80, null=True, blank=True)
    user_eq_phone = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    moh_passthrough = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    media_encryption_optimistic = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    rpid_immediate = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    g726_non_standard = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    rtp_keepalive = models.PositiveIntegerField(null=True, blank=True)
    rtp_timeout = models.PositiveIntegerField(null=True, blank=True)
    rtp_timeout_hold = models.PositiveIntegerField(null=True, blank=True)
    bind_rtp_to_media_address = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    voicemail_extension = models.CharField(max_length=40, null=True, blank=True)
    mwi_subscribe_replaces_unsolicited = models.CharField(max_length=200, null=True, blank=True, help_text='ast_bool_values')
    acl = models.CharField(max_length=40, null=True, blank=True)
    contact_deny = models.CharField(max_length=95, null=True, blank=True)
    contact_permit = models.CharField(max_length=95, null=True, blank=True)
    contact_acl = models.CharField(max_length=40, null=True, blank=True)
    subscribe_context = models.CharField(max_length=40, null=True, blank=True)
    uniqueid = models.PositiveIntegerField(unique=True, blank=True, null=True)
    fax_detect_timeout = models.PositiveIntegerField(null=True, blank=True)
    contact_user = models.CharField(max_length=80, null=True, blank=True)
    preferred_codec_only = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    asymmetric_rtp_codec = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    rtcp_mux = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    allow_overlap = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    refer_blind_progress = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    notify_early_inuse_ringing = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    max_audio_streams = models.PositiveIntegerField(null=True, blank=True)
    max_video_streams = models.PositiveIntegerField(null=True, blank=True)
    webrtc = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    dtls_fingerprint = models.CharField(max_length=200, null=True, blank=True, help_text='sha_hash_values')
    incoming_mwi_mailbox = models.CharField(max_length=40, null=True, blank=True)
    bundle = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    dtls_auto_generate_cert = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    follow_early_media_fork = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    accept_multiple_sdp_answers = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    suppress_q850_reason_headers = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    trust_connected_line = models.CharField(max_length=200, null=True, blank=True, help_text='ast_bool_values')
    send_connected_line = models.CharField(max_length=200, null=True, blank=True, help_text='ast_bool_values')
    ignore_183_without_sdp = models.CharField(max_length=200, null=True, blank=True, help_text='ast_bool_values')
    send_history_info = models.CharField(max_length=200, null=True, blank=True, help_text='ast_bool_values')


    def __str__(self):
        return self.transport

    class Meta:
        verbose_name = u'Ps_endpoints'
        verbose_name_plural = u'Ps_endpoints'
        db_table = 'ps_endpoints'



# class Cdr(models.Model):
#     calldate        = models.DateTimeField()
#     clid            = models.CharField(max_length=80, null=True, blank=True)
#     src             = models.CharField(max_length=80, null=True, blank=True)
#     dst             = models.CharField(max_length=80, null=True, blank=True)
#     dcontext        = models.CharField(max_length=80, null=True, blank=True)
#     channel         = models.CharField(max_length=80, null=True, blank=True)
#     dstchannel      = models.CharField(max_length=80, null=True, blank=True)
#     lastapp         = models.CharField(max_length=80, null=True, blank=True)
#     lastdata        = models.CharField(max_length=80, null=True, blank=True)
#     duration        = models.IntegerField(default=0, null=True, blank=True)
#     billsec         = models.IntegerField(default=0, null=True, blank=True)
#     disposition     = models.CharField(max_length=45, editable=True, default='', null=False, choices=DISPOSITIONS, db_index=True)
#     amaflags        = models.PositiveIntegerField(editable=True, default=0, null=False, choices=AMAFLAGS, db_index=True)
#     accountcode     = models.CharField(max_length=20, null=True, blank=True)
#     uniqueid        = models.AutoField(auto_created=True, primary_key=True, serialize=False, editable=True, verbose_name='Unique ID')
#     userfield       = models.CharField(max_length=255, null=True, blank=True)
#     did             = models.CharField(max_length=50, null=True, blank=True)
#     recordingfile   = models.CharField(max_length=255, null=True, blank=True)
#     cnum            = models.CharField(max_length=80, null=True, blank=True)
#     cnam            = models.CharField(max_length=80, null=True, blank=True)
#     outbound_cnum   = models.CharField(max_length=80, null=True, blank=True)
#     outbound_cnam   = models.CharField(max_length=80, null=True, blank=True)
#     dst_cnam        = models.CharField(max_length=80, null=True, blank=True)

#     class Meta:
#         db_table = 'cdr'
    
#     def billsec_norm(obj):
#         return timedelta(seconds=obj.billsec)
#     billsec_norm.short_description = u'Min.'

#     def duration_cout(self):
#         return self.duration * 2.08
    
#     def duration_cout_total(self):
#         return sum(item.duration_cout() for item in self.items.all())

class IvrDetails(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    announcement = models.IntegerField(blank=True, null=True)
    directdial = models.CharField(max_length=50, blank=True, null=True)
    invalid_loops = models.CharField(max_length=10, blank=True, null=True)
    invalid_retry_recording = models.CharField(max_length=25, blank=True, null=True)
    invalid_destination = models.CharField(max_length=50, blank=True, null=True)
    timeout_enabled = models.CharField(max_length=50, blank=True, null=True)
    invalid_recording = models.CharField(max_length=25, blank=True, null=True)
    retvm = models.CharField(max_length=8, blank=True, null=True)
    timeout_time = models.IntegerField(blank=True, null=True)
    timeout_recording = models.CharField(max_length=25, blank=True, null=True)
    timeout_retry_recording = models.CharField(max_length=25, blank=True, null=True)
    timeout_destination = models.CharField(max_length=50, blank=True, null=True)
    timeout_loops = models.CharField(max_length=10, blank=True, null=True)
    timeout_append_announce = models.IntegerField(blank=True, null=True)
    invalid_append_announce = models.IntegerField(blank=True, null=True)
    timeout_ivr_ret = models.IntegerField(blank=True, null=True)
    invalid_ivr_ret = models.IntegerField(blank=True, null=True)
    alertinfo = models.CharField(max_length=150, blank=True, null=True)
    rvolume = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        verbose_name = u'Ivr_details'
        verbose_name_plural = u'Ivr_details'
        db_table = 'ivr_details'


# class Cel(models.Model):
#     """
#        SQL CREATE TABLE cel
#     """
#     eventtime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     eventtype = models.CharField(max_length=80, default='', blank=True, null=True)
#     userdeftype = models.CharField(max_length=80, default='', blank=True, null=True)
#     cid_name = models.CharField(max_length=80, default='', blank=True, null=True)
#     cid_num = models.CharField(max_length=80, default='', blank=True, null=True)
#     cid_ani = models.CharField(max_length=80, default='', blank=True, null=True)
#     cid_rdnis = models.CharField(max_length=80, default='', blank=True, null=True)
#     cid_dnid = models.CharField(max_length=80, default='', blank=True, null=True)
#     exten = models.CharField(max_length=80, default='', blank=True, null=True)
#     context = models.CharField(max_length=80, default='', blank=True, null=True)
#     channame = models.CharField(max_length=80, default='', blank=True, null=True)
#     appname = models.CharField(max_length=80, default='', blank=True, null=True)
#     appdata = models.CharField(max_length=80, default='', blank=True, null=True)
#     accountcode = models.CharField(max_length=20, default='', blank=True, null=True)
#     peeraccount = models.CharField(max_length=80, default='', blank=True, null=True)
#     uniqueid = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Unique ID')
#     linkedid = models.CharField(max_length=80, default='', blank=True, null=True)
#     amaflags =  models.IntegerField(default=0, blank=True, null=True)
#     userfield = models.CharField(max_length=255, default='', blank=True, null=True)
#     peer = models.CharField(max_length=80, default='', blank=True, null=True)

#     def __unicode__(self, *args, **kwargs):
#         return u'%s | %s --> %s длит.: %s сек.' % (self.eventtime, self.context, self.exten, self.amaflags)


#     class Meta:
#         db_table = 'cel'

class Contacts(models.Model):
    uri = models.CharField(max_length=511, null=True, blank=True)
    expiration_time = models.IntegerField(null=True, blank=True, verbose_name='expiration_time')
    quality_frequency = models.IntegerField(null=True, blank=True, verbose_name='quality_frequency')
    outbound_proxy = models.CharField(max_length=40, null=True, blank=True)
    path = models.TextField(null=True, blank=True, verbose_name='path')
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    quality_timeout = models.FloatField(null=True, blank=True, verbose_name='quality_timeout')
    reg_server = models.CharField(max_length=255, null=True, blank=True)
    authenticate_quality = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    via_addr = models.CharField(max_length=40, null=True, blank=True)
    via_port = models.IntegerField(null=True, blank=True, verbose_name='expiration_time')
    call_id = models.CharField(max_length=255, null=True, blank=True)
    endpoint = models.CharField(max_length=40, null=True, blank=True)
    prune_on_boot = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)

    def __str__(self):
        return self.user_agent

    class Meta:
        verbose_name = u'Ps_contacts'
        verbose_name_plural = u'Ps_contacts'
        db_table = 'ps_contacts'


class AsteriskPublication(models.Model):
    devicestate_publish = models.CharField(max_length=40, null=True, blank=True)
    mailboxstate_publish = models.CharField(max_length=40, null=True, blank=True)
    device_state = models.CharField(max_length=128, choices=YES_NO, null=True, blank=True)
    device_state_filter = models.CharField(max_length=256, null=True, blank=True)
    mailbox_state = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    mailbox_state_filter = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.devicestate_publish

    class Meta:
        verbose_name = u'Ps_asterisk_publications'
        verbose_name_plural = u'Ps_asterisk_publications'
        db_table = 'ps_asterisk_publications'


class Endpoints_id_ips(models.Model):
    endpoint = models.CharField(max_length=40, null=True, blank=True)
    match = models.CharField(max_length=80, null=True, blank=True)
    srv_lookups = models.CharField(max_length=3, choices=YES_NO, null=True, blank=True)
    match_header = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.endpoint

    class Meta:
        verbose_name = u'Ps_endpoint_id_ips'
        verbose_name_plural = u'Ps_endpoint_id_ips'
        db_table = 'ps_endpoint_id_ips'


class Queue(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, serialize=False, verbose_name='Unique ID', editable=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    musiconhold = models.CharField(max_length=128, choices=MUSICONHOLD, null=True, blank=True)
    announce = models.CharField(max_length=128, null=True, blank=True)
    context = models.ForeignKey(
        Contexts, on_delete=models.CASCADE, max_length=200, db_column='context')
    timeout = models.IntegerField(null=True, blank=True)
    ringinuse = models.CharField(
        max_length=128, choices=YES_NO, null=True, blank=True)
    setinterfacevar = models.CharField(
        max_length=128, choices=YES_NO, null=True, blank=True)
    setqueueentryvar = models.CharField(
        max_length=128, choices=YES_NO, null=True, blank=True)
    monitor_format = models.CharField(max_length=8, null=True, blank=True)
    membermacro = models.CharField(max_length=512, null=True, blank=True)
    membergosub = models.CharField(max_length=512, null=True, blank=True)
    queue_youarenext = models.CharField(max_length=128, null=True, blank=True)
    queue_thereare = models.CharField(max_length=128, null=True, blank=True)
    queue_callswaiting = models.CharField(
        max_length=128, null=True, blank=True)
    queue_quantity1 = models.CharField(max_length=128, null=True, blank=True)
    queue_quantity2 = models.CharField(max_length=128, null=True, blank=True)
    queue_holdtime = models.CharField(max_length=128, null=True, blank=True)
    queue_minutes = models.CharField(max_length=128, null=True, blank=True)
    queue_minute = models.CharField(max_length=128, null=True, blank=True)
    queue_seconds = models.CharField(max_length=128, null=True, blank=True)
    queue_thankyou = models.CharField(max_length=128, null=True, blank=True)
    queue_callerannonce = models.CharField(
        max_length=128, null=True, blank=True)
    queue_reporthold = models.CharField(max_length=128, null=True, blank=True)
    annonce_frequency = models.IntegerField(null=True, blank=True)
    announce_to_first_user = models.CharField(
        max_length=128, choices=YES_NO, null=True, blank=True)
    min_announce_frequency = models.IntegerField(null=True, blank=True)
    annonce_round_seconds = models.IntegerField(null=True, blank=True)
    announce_holdtime = models.CharField(max_length=128, null=True, blank=True)
    announce_position = models.CharField(max_length=128, null=True, blank=True)
    announce_position_limit = models.IntegerField(null=True, blank=True)
    periodic_announce = models.CharField(max_length=50, null=True, blank=True)
    periodic_announce_frequency = models.IntegerField(null=True, blank=True)
    relative_periodic_announce = models.CharField(
        max_length=128, choices=YES_NO, null=True, blank=True)
    random_periodic_announce = models.CharField(
        max_length=128, choices=YES_NO, null=True, blank=True)
    retry = models.IntegerField(null=True, blank=True)
    wrapuptime = models.IntegerField(null=True, blank=True)
    penaltymemberslimit = models.IntegerField(null=True, blank=True)
    autofill = models.CharField(
        max_length=128, choices=YES_NO, null=True, blank=True)
    monitor_type = models.CharField(max_length=128, null=True, blank=True)
    autopause = models.CharField(
        max_length=128, choices=QUEUE_AUTOPAUSE, null=True, blank=True)
    autopausedelay = models.IntegerField(null=True, blank=True)
    autopausebusy = models.CharField(
        max_length=128, choices=YES_NO, null=True, blank=True)
    autopauseunavail = models.CharField(
        max_length=128, choices=YES_NO, null=True, blank=True)
    maxlen = models.IntegerField(null=True, blank=True)
    servicelevel = models.IntegerField(null=True, blank=True)
    strategy = models.CharField(
        max_length=128, choices=QUEUE_STRATEGY, null=True, blank=True)
    joinemplty = models.CharField(max_length=128, null=True, blank=True)
    leavewhenempty = models.CharField(max_length=128, null=True, blank=True)
    reportholdtime = models.CharField(
        max_length=128, choices=YES_NO, null=True, blank=True)
    memberdelay = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    timeoutrestart = models.CharField(
        max_length=128, choices=YES_NO, null=True, blank=True)
    defaultrule = models.CharField(max_length=128, null=True, blank=True)
    timeoutpriority = models.CharField(max_length=128, null=True, blank=True)

    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name = u'Queues'
        verbose_name_plural = u'Queues'
        db_table = 'queues'


class QueueMember(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, serialize=False, verbose_name='Unique ID', editable=True)
    queue_name = models.CharField(max_length=80, null=True, blank=True)
    interface = models.CharField(max_length=80, null=True, blank=True)
    membername = models.CharField(max_length=80, null=True, blank=True)
    state_interface = models.CharField(max_length=80, null=True, blank=True)
    penalty = models.IntegerField(null=True, blank=True)
    paused = models.IntegerField(null=True, blank=True)
    uniqueid = models.IntegerField(null=True, blank=True)
    wrapuptime = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.queue_name

    class Meta:
        verbose_name = u'Queue_members'
        verbose_name_plural = u'Queue_members'
        db_table = 'queue_members'


class QueuesConfig(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, serialize=False, verbose_name='Unique ID', editable=True)
    extension = models.CharField(max_length=20, blank=True, null=True)
    descr = models.CharField(max_length=35, blank=True, null=True)
    grppre = models.CharField(max_length=100, blank=True, null=True)
    alertinfo = models.CharField(max_length=254, blank=True, null=True)
    ringing = models.IntegerField(blank=True, null=True)
    maxwait = models.CharField(max_length=8, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    ivr_id = models.CharField(max_length=8, blank=True, null=True)
    dest = models.CharField(max_length=50, blank=True, null=True)
    cwignore = models.IntegerField(blank=True, null=True)
    queuewait = models.IntegerField(blank=True, null=True)
    use_queue_context = models.IntegerField(blank=True, null=True)
    togglehint = models.IntegerField(blank=True, null=True)
    qnoanswer = models.IntegerField(blank=True, null=True)
    callconfirm = models.IntegerField(blank=True, null=True)
    callconfirm_id = models.IntegerField(blank=True, null=True)
    qregex = models.CharField(max_length=255, blank=True, null=True)
    agentannounce_id = models.IntegerField(blank=True, null=True)
    joinannounce_id = models.IntegerField(blank=True, null=True)
    monitor_type = models.CharField(max_length=5, blank=True, null=True)
    monitor_heard = models.IntegerField(blank=True, null=True)
    monitor_spoken = models.IntegerField(blank=True, null=True)
    callback_id = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        db_table = 'queues_config'


class QueueRules(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, serialize=False, verbose_name='Unique ID', editable=True)
    rule_name = models.CharField(max_length=80, blank=True, null=True)
    time = models.CharField(max_length=32, blank=True, null=True)
    min_penalty = models.CharField(max_length=32, blank=True, null=True)
    max_penalty = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.rule_name

    class Meta:
        verbose_name = u'Queues_rules'
        verbose_name_plural = u'Queues_rules'
        db_table = 'queues_rules'

class QueueLog(models.Model):
    time = models.CharField(max_length=20, blank=False, null=True, editable=False, db_index=True)
    callid = models.CharField(max_length=32, blank=True, null=False, editable=False, db_index=True)
    queue = models.CharField(max_length=32, blank=True, null=False, editable=False, db_index=True, db_column='queuename')
    agent = models.CharField(max_length=32, blank=True, null=False, editable=False, db_index=True)
    event = models.CharField(max_length=32, blank=True, null=False, editable=False, db_index=True)
    data = models.TextField(blank=True, null=False, editable=False)

    class Meta:
        db_table = 'queues_log'

    def __unicode__(self):
        time = datetime.fromtimestamp(float(self.time)).strftime('%Y-%m-%d %H:%M:%S')
        call = Cdr.objects.get(uniqueid=self.callid)
        return u'%s' % (call)


class Sip_conf(models.Model):
    """
        Sip 
    """
    id = models.BigIntegerField(unique=True, primary_key=True, serialize=False, verbose_name='Unique ID', editable=True)
    name = models.CharField(max_length=15, help_text='Numéro')
    host = models.CharField(max_length=25, default='dynamic',
                            help_text='Liaison à un hôte ou une adresse IP spécifique, ou \'dynamique \'')
    nat = models.CharField(max_length=5, default='no',
                           help_text='Autoriser ou non le travail via NAT', choices=NAT)
    type = models.CharField(max_length=8, default='friend',
                            help_text='Type d\'utilisateur', choices=TYPE_SIP)
    accountcode = models.CharField(max_length=20, null=True, blank=True)
    amaflags = models.CharField(max_length=20, default='billing', blank=True, null=True,
                                help_text='indicateurs spéciaux pour contrôler le calcul par défaut', choices=AMAFLAGS)
    callgroup = models.CharField(
        max_length=40, blank=True, null=True, help_text='callgroup')
    callerid = models.CharField(max_length=250, blank=True, null=True,
                                help_text='Laisser vide pour l\'auto-substitution')
    cancallforward = models.CharField(max_length=3, default='yes', blank=False,
                                      null=False, help_text='autoriser ou non le transfert d\'appel', choices=YES_NO)
    directmedia = models.CharField(
        max_length=6, default='no', choices=DIRECTMEDIA, help_text='Autoriser ou non le trafic direct')
    context = models.ForeignKey(Contexts, on_delete=models.CASCADE,
                                blank=True, null=True, help_text='le contexte', db_column='context')
    defaultip = models.CharField(max_length=25, blank=True, null=True, help_text='Si vous connaissez l\'adresse IP du téléphone, vous pouvez la saisir ici. Ces paramètres seront utilisés lors des appels vers ce téléphone s\'il n\'est pas déjà enregistré auprès du serveur. Après l\'enregistrement, le téléphone lui-même indiquera à Asterisk sous quel nom d\'utilisateur et quelle adresse IP il est disponible.')
    dtmfmode = models.CharField(max_length=10, choices=DTMFMODE_SIP, help_text='En mode automatique, Asterisk utilisera le mode rfc2833 pour la transmission DTMF, par défaut, mais passera en mode intrabande pour les signaux DTMF, si le client distant n`\'indique pas dans le message SDP qu\'il prend en charge le mode de transmission DTMF - rfc2833')
    fromuser = models.CharField(
        max_length=80, blank=True, null=True, help_text='')
    fromdomain = models.CharField(
        max_length=80, blank=True, null=True, help_text='')
    insecure = models.CharField(
        max_length=20, default='', blank=True, null=True, help_text='ignorer', choices=INVITE)
    language = models.CharField(
        max_length=2,  default='fr', help_text='langue')
    mailbox = models.CharField(max_length=15, blank=False, null=True,
                               help_text='Laisser vide pour l\'auto-substitution')
    md5secret = models.CharField(
        max_length=80, blank=True, null=True, help_text='Mot de passe MD5')
    deny = models.CharField(max_length=25, blank=True,
                            null=True, help_text='sous-réseaux interdits')
    permit = models.CharField(
        max_length=25, blank=True, null=True, help_text='sous-réseaux autorisés')
    mask = models.CharField(max_length=25, blank=True,
                            null=True, help_text='obsolète')
    musiconhold = models.CharField(max_length=100, db_column='musiconhold', choices=MUSICONHOLD,
                                   blank=True, null=True, help_text='musique en attente', db_index=True)
    pickupgroup = models.CharField(
        max_length=80, blank=True, null=True, help_text='')
    qualify = models.CharField(max_length=5, default='no', blank=False, null=False, help_text='si oui, Asterisk enverra périodiquement (une fois toutes les 2 secondes) un message OPTIONS SIP pour vérifier que cet appareil fonctionne et qu\'il est disponible pour passer des appels. Si un appareil donné ne répond pas dans un délai spécifié, Asterisk considère que cet appareil est éteint et indisponible pour passer des appels.', choices=YES_NO)
    regexten = models.CharField(
        max_length=80, blank=True, null=True, help_text='')
    restrictcid = models.CharField(
        max_length=25, blank=True, null=True, help_text='obsolète')
    rtptimeout = models.CharField(
        max_length=3, blank=True, null=True, help_text='')
    rtpholdtimeout = models.CharField(
        max_length=3, blank=True, null=True, help_text='')
    secret = models.CharField(
        max_length=15, blank=True, null=False,  help_text='Laisser vide pour générer')
    setvar = models.CharField(
        max_length=25, blank=True, null=True, help_text='obsolète')
    disallow = models.CharField(
        max_length=100,  default='all', help_text='codecs interdits')
    allow = models.CharField(
        max_length=100,  default='alaw', help_text='codecs autorisés')
    comment = models.TextField(blank=True, null=True, help_text='commenter')
    trustrpid = models.CharField(max_length=3, blank=True, null=True, default='no', choices=YES_NO,
                                 help_text='Puis-je faire confiance à l\'ID de partie distante reçu du client SIP')
    sendrpid = models.CharField(max_length=3, blank=True, null=True, default='yes', choices=YES_NO,
                                help_text='Il est nécessaire de transférer le SIP vers le client Remote-Party-ID')
    videosupport = models.CharField(
        max_length=3, blank=True, null=True, default='no', choices=YES_NO, help_text='Support vidéo')
    fullcontact = models.CharField(
        max_length=80, blank=True, null=True, help_text='fullcontact')
    ipaddr = models.GenericIPAddressField(
        blank=True, null=True, help_text='Pour la compatibilité')
    port = models.PositiveIntegerField(
        blank=True, null=True, help_text='Port de clients non dynamiques')
    regseconds = models.BigIntegerField(
        blank=True, null=True, help_text='Pour la compatibilité')
    username = models.CharField(
        max_length=100, blank=True, null=True, help_text='username')
    regserver = models.CharField(
        max_length=100, blank=True, null=True, help_text='regserver')
    useragent = models.CharField(
        max_length=100, blank=True, null=True, help_text='useragent')
    lastms = models.CharField(
        max_length=100, blank=True, null=True, help_text='lastms')
    defaultuser = models.CharField(max_length=15, blank=True, null=True,
                                   help_text='Le serveur Asterisk enverra des INVITE à username@defaultip')

    def __str__(self):
        return u'%s (%s)' % (self.name, self.accountcode)

    # def gen_passwd(self):
    #     self.secret = ''.join(
    #         choice(string.letters.lower()+string.digits) for i in range(12))
    #     return self.save()

    # def __init__(self, *args, **kwargs):
    #     super(Sip_conf, self).__init__(*args, **kwargs)
    #     if not self.secret.__len__():
    #         self.gen_passwd()

    class Meta:
        db_table = 'sip_conf'


class Sippeers(models.Model):
    """
        Sippeers
    """
    id = models.BigIntegerField(unique=True, primary_key=True, serialize=False, verbose_name='Unique ID', editable=True)
    name = models.CharField(max_length=15, help_text='Numéro')
    ipaddr = models.GenericIPAddressField(
        blank=True, null=True, help_text='Addresse IP')
    port = models.PositiveIntegerField(
        blank=True, null=True, help_text='Port de clients non dynamiques')
    regseconds = models.BigIntegerField(
        blank=True, null=True, help_text='regseconds')
    defaultuser = models.CharField(max_length=15, blank=True, null=True,
                                   help_text='Le serveur Asterisk enverra des INVITE à username@defaultip')
    fullcontact = models.CharField(
        max_length=100, blank=True, null=True, help_text='fullcontact')
    regserver = models.CharField(
        max_length=20, blank=True, null=True, help_text='regserver')
    useragent = models.CharField(
        max_length=20, blank=True, null=True, help_text='useragent')
    lastms = models.CharField(
        max_length=100, blank=True, null=True, help_text='lastms')
    host = models.CharField(max_length=25, default='dynamic', blank=True, null=True,
                            help_text='Liaison à un hôte ou une adresse IP spécifique, ou \'dynamique \'')
    type = models.CharField(max_length=8, default='friend', blank=True,
                            null=True, help_text='Type d\'utilisateur', choices=TYPE_SIP)
    context = models.ForeignKey(Contexts, on_delete=models.CASCADE,
                                blank=True, null=True, help_text='le contexte', db_column='context')
    permit = models.CharField(
        max_length=25, blank=True, default='0.0.0.0/0', null=True, help_text='sous-réseaux autorisés')
    deny = models.CharField(max_length=25, default='0.0.0.0/0', blank=True,
                            null=True, help_text='sous-réseaux interdits')
    secret = models.CharField(
        max_length=15, blank=True, null=True, help_text='Laisser vide pour générer')
    md5secret = models.CharField(max_length=40, blank=True, null=True)
    remotesecret = models.CharField(max_length=40, blank=True, null=True)
    dtmfmode = models.CharField(max_length=10, blank=True, null=True, choices=DTMFMODE_SIP,
                                help_text='En mode automatique, Asterisk utilisera le mode rfc2833 pour la transmission DTMF, par défaut, mais passera en mode intrabande pour les signaux DTMF, si le client distant n`\'indique pas dans le message SDP qu\'il prend en charge le mode de transmission DTMF - rfc2833')
    transport = models.CharField(max_length=40, blank=True, null=True, choices=TRANSPORT_SIP,
                                 help_text='Transport des données')
    directmedia = models.CharField(max_length=6, default='no', blank=True, null=True,
                                   choices=DIRECTMEDIA, help_text='Autoriser ou non le trafic direct')
    nat = models.CharField(max_length=5, default='no', blank=True, null=True,
                           choices=NAT, help_text='Autoriser ou non le travail via NAT')
    callgroup = models.CharField(
        max_length=40, blank=True, null=True, help_text='callgroup')
    callingpres = models.CharField(
        blank=True, null=True, choices=CALLINGPRES, help_text='Type de transport')
    pickupgroup = models.CharField(max_length=40, blank=True, null=True)
    language = models.CharField(max_length=40, blank=True, null=True)
    disallow = models.CharField(
        max_length=40,  default='all', null=True, help_text='codecs interdits')
    allow = models.CharField(
        max_length=40,  default='all', null=True, help_text='codecs autorisés')
    insecure = models.CharField(
        max_length=20, default='', blank=True, null=True, help_text='ignorer', choices=INVITE)
    trustrpid = models.CharField(max_length=3, blank=True, null=True, default='no', choices=YES_NO,
                                 help_text='Puis-je faire confiance à l\'ID de partie distante reçu du client SIP')
    progressinband = models.CharField(
        max_length=20, default='', blank=True, null=True, help_text='ignorer', choices=PROGRESSINBAND)
    promiscredir = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    useclientcode = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    accountcode = models.CharField(max_length=40, blank=True, null=True)
    setvar = models.CharField(max_length=40, blank=True, null=True)
    callerid = models.CharField(max_length=40, blank=True, null=True)
    amaflags = models.CharField(max_length=40, blank=True, null=True)
    callcounter = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    busylevel = models.PositiveIntegerField(
        blank=True, null=True, help_text='')
    allowoverlap = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    allowsubscribe = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    videosupport = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    maxcallbitrate = models.PositiveIntegerField(
        blank=True, null=True, help_text='')
    rfc2833compensate = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    mailbox = models.CharField(max_length=40, help_text='101@default',)
    session_timers = models.CharField(
        max_length=10, blank=True, null=True, choices=SESSIONTIMERS, help_text='', db_column='session-timers')
    session_expires = models.PositiveIntegerField(
        blank=True, null=True, help_text='', db_column='session-expires')
    session_minse = models.PositiveIntegerField(
        blank=True, null=True, help_text='', db_column='session-minse')
    session_refresher = models.CharField(
        max_length=3, blank=True, null=True, choices=SESSIONREFRESHER, help_text='', db_column='session-refresher')
    t38pt_usertpsource = models.CharField(max_length=40, blank=True, null=True)
    regexten = models.CharField(max_length=40, blank=True, null=True)
    fromdomain = models.CharField(max_length=40, blank=True, null=True)
    fromuser = models.CharField(max_length=40, blank=True, null=True)
    qualify = models.CharField(max_length=40, blank=True, null=True)
    defaultip = models.CharField(max_length=40, blank=True, null=True)
    rtptimeout = models.PositiveIntegerField(
        blank=True, null=True, help_text='')
    rtpholdtimeout = models.PositiveIntegerField(
        blank=True, null=True, help_text='')
    sendrpid = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    outboundproxy = models.CharField(max_length=40, blank=True, null=True)
    callbackextension = models.CharField(max_length=40, blank=True, null=True)
    timert1 = models.PositiveIntegerField(blank=True, null=True, help_text='')
    timerb = models.PositiveIntegerField(blank=True, null=True, help_text='')
    qualifyfreq = models.PositiveIntegerField(
        blank=True, null=True, help_text='')
    constantssrc = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    contactpermit = models.CharField(max_length=40, blank=True, null=True)
    contactdeny = models.CharField(max_length=40, blank=True, null=True)
    usereqphone = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    textsupport = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    faxdetect = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    buggymwi = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    auth = models.CharField(max_length=40, blank=True, null=True)
    fullname = models.CharField(max_length=40, blank=True, null=True)
    trunkname = models.CharField(max_length=40, blank=True, null=True)
    cid_number = models.CharField(max_length=40, blank=True, null=True)
    callingpres = models.CharField(
        max_length=25, blank=True, null=True, choices=CALLINGPRES, help_text='callingpres')
    mohinterpret = models.CharField(max_length=40, blank=True, null=True)
    mohsuggest = models.CharField(max_length=40, blank=True, null=True)
    parkinglot = models.CharField(max_length=40, blank=True, null=True)
    hasvoicemail = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    subscribemwi = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    vmexten = models.CharField(max_length=40, blank=True, null=True)
    autoframing = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    rtpkeepalive = models.PositiveIntegerField(
        blank=True, null=True, help_text='')
    call_limit = models.PositiveIntegerField(
        blank=True, null=True, help_text='', db_column='call-limit')
    g726nonstandard = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    ignoresdpversion = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    allowtransfer = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')
    dynamic = models.CharField(
        max_length=3, blank=True, null=True, choices=YES_NO, help_text='')

    def __str__(self):
        return '%s %s' % (self.fullname, self.name)

    # def gen_passwd(self):
    #     self.secret = ''.join(
    #         choice(string.letters.lower()+string.digits) for i in xrange(12))
    #     return self.save()

    # def __init__(self, *args, **kwargs):
    #     super(Sippeers, self).__init__(*args, **kwargs)
    #     if not self.secret.__len__():
    #         self.gen_passwd()

    class Meta:
        verbose_name = u'Sippeers'
        verbose_name_plural = u'Sippeers'
        db_table = 'sippeers'


class VoiceMail(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True,
                             serialize=False, verbose_name='Unique ID', editable=True)
    uniqueid = models.IntegerField(null=True, blank=True)
    context = models.ForeignKey(Contexts, on_delete=models.CASCADE, blank=True, null=True, help_text='le contexte', db_column='context')
    mailbox = models.CharField(max_length=80, null=True, blank=True)
    password = models.CharField(max_length=80, null=True, blank=True)
    fullname = models.CharField(max_length=80, null=True, blank=True)
    alias = models.CharField(max_length=80, null=True, blank=True)
    email = models.CharField(max_length=80, null=True, blank=True)
    pager = models.CharField(max_length=80, null=True, blank=True)
    attach = models.CharField(max_length=128, choices=YES_NO, null=True, blank=True)
    attachfmt = models.CharField(max_length=10, null=True, blank=True)
    servermail = models.CharField(max_length=80, null=True, blank=True)
    language = models.CharField(max_length=20, null=True, blank=True)
    tz = models.CharField(max_length=30, null=True, blank=True)
    deletevoicemail = models.CharField(max_length=128, choices=YES_NO, null=True, blank=True)   
    sayid = models.CharField(max_length=128, choices=YES_NO, null=True, blank=True)
    saycid = models.CharField(max_length=128, choices=YES_NO, null=True, blank=True)
    sendvoicemail = models.CharField(max_length=128, choices=YES_NO, null=True, blank=True)
    review = models.CharField(max_length=128, choices=YES_NO, null=True, blank=True)
    tempgreetwarn = models.CharField(max_length=128, choices=YES_NO, null=True, blank=True)
    operator = models.CharField(max_length=128, choices=YES_NO, null=True, blank=True)
    envelope = models.CharField(max_length=128, choices=YES_NO, null=True, blank=True)
    sayduration = models.IntegerField(null=True, blank=True)
    forcename = models.CharField(max_length=200, choices=YES_NO, null=True, blank=True)
    forcegreetings = models.CharField(max_length=200, choices=YES_NO, null=True, blank=True)
    callback = models.CharField(max_length=80, null=True, blank=True)
    dialout = models.CharField(max_length=80, null=True, blank=True)
    exitcontext = models.CharField(max_length=80, null=True, blank=True)
    maxmsg = models.IntegerField(null=True, blank=True)
    volgain = models.IntegerField(null=True, blank=True)
    imapuser = models.CharField(max_length=80, null=True, blank=True)
    imappassword = models.CharField(max_length=80, null=True, blank=True)
    imapserver = models.CharField(max_length=80, null=True, blank=True)
    imapport = models.CharField(max_length=8, null=True, blank=True)
    imapflags = models.CharField(max_length=80, null=True, blank=True)
    stamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.fullname

    class Meta:
        db_table = 'voicemail'
