from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User


from issabel.models import Cdr, Cel
from agenda.models import Note
from contacts.models import Contact
from accounts.models import Profile

from acquisition.models import Acquisition
from commprom.models import Commprom
from dat.models import Dat
from recouvrement.models import Recouvrement
from renouvellement.models import Renouvellement
from comptedormant.models import Compte_dormant

# Create your views here.

# STATUTS
statut_1  = 'Statuts de reporting'
statut_2  = 'Accord'
statut_3  = 'Déjà payé son crédit'
statut_4  = 'Refus'
statut_5  = 'Rappel'
statut_6  = 'Injoignable'
statut_7  = 'Absent'
statut_8  = 'Faux numéro'
statut_9  = 'Réfléchir'


# ANSWERED
# BUSY
# FAILED
# CONGESTION
# NO ANSWER

@login_required
def dashboard_view(request):
    
    # online
    users_online = Profile.objects.filter(is_online=True).count()
    user_list = User.objects.all()

    user = request.user
    # report CDR 
    cdr_answered = Cdr.objects.filter(src=user).filter(disposition='ANSWERED').count()
    cdr_busy = Cdr.objects.filter(src=user).filter(disposition='BUSY').count()
    cdr_failed = Cdr.objects.filter(src=user).filter(disposition='FAILED').count()
    cdr_congestion = Cdr.objects.filter(src=user).filter(disposition='CONGESTION').count()
    cdr_total = Cdr.objects.filter(src=user).count()
    cdr_list = Cdr.objects.filter(src=user).order_by('-calldate')[:5]

    # Notes
    note_nbr = Note.objects.filter(user=user).order_by('-created_date').count()

    # Scripting
    acquisition_total = Acquisition.objects.filter(user=user).count()
    commprom_total = Commprom.objects.filter(user=user).count()
    dat_total = Dat.objects.filter(user=user).count()
    recouvrement_total = Recouvrement.objects.filter(user=user).count()
    renouvellement_total = Renouvellement.objects.filter(user=user).count()
    compte_dormant_total= Compte_dormant.objects.filter(user=user).count()

    acquisition_1_user = Acquisition.objects.filter(user=user).filter(Statut=statut_1).count()
    acquisition_2_user = Acquisition.objects.filter(user=user).filter(Statut=statut_2).count()
    acquisition_3_user = Acquisition.objects.filter(user=user).filter(Statut=statut_3).count()
    acquisition_4_user = Acquisition.objects.filter(user=user).filter(Statut=statut_4).count()
    acquisition_5_user = Acquisition.objects.filter(user=user).filter(Statut=statut_5).count()
    acquisition_6_user = Acquisition.objects.filter(user=user).filter(Statut=statut_6).count()
    acquisition_7_user = Acquisition.objects.filter(user=user).filter(Statut=statut_7).count()
    acquisition_8_user = Acquisition.objects.filter(user=user).filter(Statut=statut_8).count()
    acquisition_9_user = Acquisition.objects.filter(user=user).filter(Statut=statut_9).count()

    commprom_1_user = Commprom.objects.filter(user=user).filter(Statut=statut_1).count()
    commprom_2_user = Commprom.objects.filter(user=user).filter(Statut=statut_2).count()
    commprom_3_user = Commprom.objects.filter(user=user).filter(Statut=statut_3).count()
    commprom_4_user = Commprom.objects.filter(user=user).filter(Statut=statut_4).count()
    commprom_5_user = Commprom.objects.filter(user=user).filter(Statut=statut_5).count()
    commprom_6_user = Commprom.objects.filter(user=user).filter(Statut=statut_6).count()
    commprom_7_user = Commprom.objects.filter(user=user).filter(Statut=statut_7).count()
    commprom_8_user = Commprom.objects.filter(user=user).filter(Statut=statut_8).count()
    commprom_9_user = Commprom.objects.filter(user=user).filter(Statut=statut_9).count()

    dat_1_user = Dat.objects.filter(user=user).filter(Statut=statut_1).count()
    dat_2_user = Dat.objects.filter(user=user).filter(Statut=statut_2).count()
    dat_3_user = Dat.objects.filter(user=user).filter(Statut=statut_3).count()
    dat_4_user = Dat.objects.filter(user=user).filter(Statut=statut_4).count()
    dat_5_user = Dat.objects.filter(user=user).filter(Statut=statut_5).count()
    dat_6_user = Dat.objects.filter(user=user).filter(Statut=statut_6).count()
    dat_7_user = Dat.objects.filter(user=user).filter(Statut=statut_7).count()
    dat_8_user = Dat.objects.filter(user=user).filter(Statut=statut_8).count()
    dat_9_user = Dat.objects.filter(user=user).filter(Statut=statut_9).count()

    recouvrement_1_user = Recouvrement.objects.filter(user=user).filter(Statut=statut_1).count()
    recouvrement_2_user = Recouvrement.objects.filter(user=user).filter(Statut=statut_2).count()
    recouvrement_3_user = Recouvrement.objects.filter(user=user).filter(Statut=statut_3).count()
    recouvrement_4_user = Recouvrement.objects.filter(user=user).filter(Statut=statut_4).count()
    recouvrement_5_user = Recouvrement.objects.filter(user=user).filter(Statut=statut_5).count()
    recouvrement_6_user = Recouvrement.objects.filter(user=user).filter(Statut=statut_6).count()
    recouvrement_7_user = Recouvrement.objects.filter(user=user).filter(Statut=statut_7).count()
    recouvrement_8_user = Recouvrement.objects.filter(user=user).filter(Statut=statut_8).count()
    recouvrement_9_user = Recouvrement.objects.filter(user=user).filter(Statut=statut_9).count()

    renouvellement_1_user = Renouvellement.objects.filter(user=user).filter(Statut=statut_1).count()
    renouvellement_2_user = Renouvellement.objects.filter(user=user).filter(Statut=statut_2).count()
    renouvellement_3_user = Renouvellement.objects.filter(user=user).filter(Statut=statut_3).count()
    renouvellement_4_user = Renouvellement.objects.filter(user=user).filter(Statut=statut_4).count()
    renouvellement_5_user = Renouvellement.objects.filter(user=user).filter(Statut=statut_5).count()
    renouvellement_6_user = Renouvellement.objects.filter(user=user).filter(Statut=statut_6).count()
    renouvellement_7_user = Renouvellement.objects.filter(user=user).filter(Statut=statut_7).count()
    renouvellement_8_user = Renouvellement.objects.filter(user=user).filter(Statut=statut_8).count()
    renouvellement_9_user = Renouvellement.objects.filter(user=user).filter(Statut=statut_9).count()

    compte_dormant__1_user = Compte_dormant.objects.filter(user=user).filter(Statut=statut_1).count()
    compte_dormant__2_user = Compte_dormant.objects.filter(user=user).filter(Statut=statut_2).count()
    compte_dormant__3_user = Compte_dormant.objects.filter(user=user).filter(Statut=statut_3).count()
    compte_dormant__4_user = Compte_dormant.objects.filter(user=user).filter(Statut=statut_4).count()
    compte_dormant__5_user = Compte_dormant.objects.filter(user=user).filter(Statut=statut_5).count()
    compte_dormant__6_user = Compte_dormant.objects.filter(user=user).filter(Statut=statut_6).count()
    compte_dormant__7_user = Compte_dormant.objects.filter(user=user).filter(Statut=statut_7).count()
    compte_dormant__8_user = Compte_dormant.objects.filter(user=user).filter(Statut=statut_8).count()
    compte_dormant__9_user = Compte_dormant.objects.filter(user=user).filter(Statut=statut_9).count()
    
    context = {
        'user_list': user_list,
        'users_online': users_online,
        'cdr_answered': cdr_answered,
        'cdr_busy': cdr_busy,
        'cdr_failed': cdr_failed,
        'cdr_congestion': cdr_congestion,
        'cdr_total': cdr_total,
        'cdr_list': cdr_list,

        'note_nbr': note_nbr,

        'acquisition_total': acquisition_total,
        'commprom_total': commprom_total,
        'dat_total': dat_total,
        'recouvrement_total': recouvrement_total,
        'renouvellement_total': renouvellement_total,
        'compte_dormant_total': compte_dormant_total,


        'acquisition_1_user': acquisition_1_user,
        'acquisition_2_user': acquisition_2_user,
        'acquisition_3_user': acquisition_3_user,
        'acquisition_4_user': acquisition_4_user,
        'acquisition_5_user': acquisition_5_user,
        'acquisition_6_user': acquisition_6_user,
        'acquisition_7_user': acquisition_7_user,
        'acquisition_8_user': acquisition_8_user,
        'acquisition_9_user': acquisition_9_user,

        'commprom_1_user': commprom_1_user,
        'commprom_2_user': commprom_2_user,
        'commprom_3_user': commprom_3_user,
        'commprom_4_user': commprom_4_user,
        'commprom_5_user': commprom_5_user,
        'commprom_6_user': commprom_6_user,
        'commprom_7_user': commprom_7_user,
        'commprom_8_user': commprom_8_user,
        'commprom_9_user': commprom_9_user,

        'dat_1_user': dat_1_user,
        'dat_2_user': dat_2_user,
        'dat_3_user': dat_3_user,
        'dat_4_user': dat_4_user,
        'dat_5_user': dat_5_user,
        'dat_6_user': dat_6_user,
        'dat_7_user': dat_7_user,
        'dat_8_user': dat_8_user,
        'dat_9_user': dat_9_user,

        'recouvrement_1_user': recouvrement_1_user,
        'recouvrement_2_user': recouvrement_2_user,
        'recouvrement_3_user': recouvrement_3_user,
        'recouvrement_4_user': recouvrement_4_user,
        'recouvrement_5_user': recouvrement_5_user,
        'recouvrement_6_user': recouvrement_6_user,
        'recouvrement_7_user': recouvrement_7_user,
        'recouvrement_8_user': recouvrement_8_user,
        'recouvrement_9_user': recouvrement_9_user,

        'renouvellement_1_user': renouvellement_1_user,
        'renouvellement_2_user': renouvellement_2_user,
        'renouvellement_3_user': renouvellement_3_user,
        'renouvellement_4_user': renouvellement_4_user,
        'renouvellement_5_user': renouvellement_5_user,
        'renouvellement_6_user': renouvellement_6_user,
        'renouvellement_7_user': renouvellement_7_user,
        'renouvellement_8_user': renouvellement_8_user,
        'renouvellement_9_user': renouvellement_9_user,

        'compte_dormant__1_user': compte_dormant__1_user,
        'compte_dormant__2_user': compte_dormant__2_user,
        'compte_dormant__3_user': compte_dormant__3_user,
        'compte_dormant__4_user': compte_dormant__4_user,
        'compte_dormant__5_user': compte_dormant__5_user,
        'compte_dormant__6_user': compte_dormant__6_user,
        'compte_dormant__7_user': compte_dormant__7_user,
        'compte_dormant__8_user': compte_dormant__8_user,
        'compte_dormant__9_user': compte_dormant__9_user,


    }
    template_name = 'pages/dashboard/dashboard_view.html'
    return render(request, template_name, context)


@login_required
def dashboard_admin_view(request):

    user = request.user
    users_online = Profile.objects.filter(is_online=True).count()
    user_list = User.objects.all().count()
    # report CDR 
    cdr_answered = Cdr.objects.all().filter(disposition='ANSWERED').count()
    cdr_busy = Cdr.objects.all().filter(disposition='BUSY').count()
    cdr_failed = Cdr.objects.all().filter(disposition='FAILED').count()
    cdr_congestion = Cdr.objects.all().filter(disposition='CONGESTION').count()
    cdr_total = Cdr.objects.all().count()
    cdr_list = Cdr.objects.all().order_by('-calldate')[:5] 
    cdr_duration = Cdr.objects.all().order_by('-calldate')[:1]


    # Notes
    note_nbr = Note.objects.all().count()

    # Contacts
    contact_list = Contact.objects.all().count()

    # Scripting
    acquisition_total = Acquisition.objects.all().count()
    commprom_total = Commprom.objects.all().count()
    dat_total = Dat.objects.all().count()
    recouvrement_total = Recouvrement.objects.all().count()
    renouvellement_total = Renouvellement.objects.all().count()
    compte_dormant_total= Compte_dormant.objects.all().count()

    acquisition_1 = Acquisition.objects.filter(Statut=statut_1).count()
    acquisition_2 = Acquisition.objects.filter(Statut=statut_2).count()
    acquisition_3 = Acquisition.objects.filter(Statut=statut_3).count()
    acquisition_4 = Acquisition.objects.filter(Statut=statut_4).count()
    acquisition_5 = Acquisition.objects.filter(Statut=statut_5).count()
    acquisition_6 = Acquisition.objects.filter(Statut=statut_6).count()
    acquisition_7 = Acquisition.objects.filter(Statut=statut_7).count()
    acquisition_8 = Acquisition.objects.filter(Statut=statut_8).count()
    acquisition_9 = Acquisition.objects.filter(Statut=statut_9).count()

    commprom_1 = Commprom.objects.filter(Statut=statut_1).count()
    commprom_2 = Commprom.objects.filter(Statut=statut_2).count()
    commprom_3 = Commprom.objects.filter(Statut=statut_3).count()
    commprom_4 = Commprom.objects.filter(Statut=statut_4).count()
    commprom_5 = Commprom.objects.filter(Statut=statut_5).count()
    commprom_6 = Commprom.objects.filter(Statut=statut_6).count()
    commprom_7 = Commprom.objects.filter(Statut=statut_7).count()
    commprom_8 = Commprom.objects.filter(Statut=statut_8).count()
    commprom_9 = Commprom.objects.filter(Statut=statut_9).count()  

    dat_1 = Dat.objects.filter(Statut=statut_1).count()
    dat_2 = Dat.objects.filter(Statut=statut_2).count()
    dat_3 = Dat.objects.filter(Statut=statut_3).count()
    dat_4 = Dat.objects.filter(Statut=statut_4).count()
    dat_5 = Dat.objects.filter(Statut=statut_5).count()
    dat_6 = Dat.objects.filter(Statut=statut_6).count()
    dat_7 = Dat.objects.filter(Statut=statut_7).count()
    dat_8 = Dat.objects.filter(Statut=statut_8).count()
    dat_9 = Dat.objects.filter(Statut=statut_9).count()

    recouvrement_1 = Recouvrement.objects.filter(Statut=statut_1).count()
    recouvrement_2 = Recouvrement.objects.filter(Statut=statut_2).count()
    recouvrement_3 = Recouvrement.objects.filter(Statut=statut_3).count()
    recouvrement_4 = Recouvrement.objects.filter(Statut=statut_4).count()
    recouvrement_5 = Recouvrement.objects.filter(Statut=statut_5).count()
    recouvrement_6 = Recouvrement.objects.filter(Statut=statut_6).count()
    recouvrement_7 = Recouvrement.objects.filter(Statut=statut_7).count()
    recouvrement_8 = Recouvrement.objects.filter(Statut=statut_8).count()
    recouvrement_9 = Recouvrement.objects.filter(Statut=statut_9).count()

    renouvellement_1 = Renouvellement.objects.filter(Statut=statut_1).count()
    renouvellement_2 = Renouvellement.objects.filter(Statut=statut_2).count()
    renouvellement_3 = Renouvellement.objects.filter(Statut=statut_3).count()
    renouvellement_4 = Renouvellement.objects.filter(Statut=statut_4).count()
    renouvellement_5 = Renouvellement.objects.filter(Statut=statut_5).count()
    renouvellement_6 = Renouvellement.objects.filter(Statut=statut_6).count()
    renouvellement_7 = Renouvellement.objects.filter(Statut=statut_7).count()
    renouvellement_8 = Renouvellement.objects.filter(Statut=statut_8).count()
    renouvellement_9 = Renouvellement.objects.filter(Statut=statut_9).count()

    compte_dormant__1 = Compte_dormant.objects.filter(Statut=statut_1).count()
    compte_dormant__2 = Compte_dormant.objects.filter(Statut=statut_2).count()
    compte_dormant__3 = Compte_dormant.objects.filter(Statut=statut_3).count()
    compte_dormant__4 = Compte_dormant.objects.filter(Statut=statut_4).count()
    compte_dormant__5 = Compte_dormant.objects.filter(Statut=statut_5).count()
    compte_dormant__6 = Compte_dormant.objects.filter(Statut=statut_6).count()
    compte_dormant__7 = Compte_dormant.objects.filter(Statut=statut_7).count()
    compte_dormant__8 = Compte_dormant.objects.filter(Statut=statut_8).count()
    compte_dormant__9 = Compte_dormant.objects.filter(Statut=statut_9).count()



    context = {
        'users_online': users_online,
        'user_list': user_list,
        'cdr_answered': cdr_answered,
        'cdr_busy': cdr_busy,
        'cdr_failed': cdr_failed,
        'cdr_congestion': cdr_congestion,
        'cdr_total': cdr_total,
        'cdr_list': cdr_list,
        'cdr_duration': cdr_duration,

        'note_nbr': note_nbr,
        'contact_list': contact_list,

        'acquisition_total': acquisition_total,
        'commprom_total': commprom_total,
        'dat_total': dat_total,
        'recouvrement_total': recouvrement_total,
        'renouvellement_total': renouvellement_total,
        'compte_dormant_total': compte_dormant_total,

        'acquisition_1': acquisition_1,
        'acquisition_2': acquisition_2,
        'acquisition_3': acquisition_3,
        'acquisition_4': acquisition_4,
        'acquisition_5': acquisition_5,
        'acquisition_6': acquisition_6,
        'acquisition_7': acquisition_7,
        'acquisition_8': acquisition_8,
        'acquisition_9': acquisition_9,

        'commprom_1': commprom_1,
        'commprom_2': commprom_2,
        'commprom_3': commprom_3,
        'commprom_4': commprom_4,
        'commprom_5': commprom_5,
        'commprom_6': commprom_6,
        'commprom_7': commprom_7,
        'commprom_8': commprom_8,
        'commprom_9': commprom_9,     

        'dat_1': dat_1,
        'dat_2': dat_2,
        'dat_3': dat_3,
        'dat_4': dat_4,
        'dat_5': dat_5,
        'dat_6': dat_6,
        'dat_7': dat_7,
        'dat_8': dat_8,
        'dat_9': dat_9,     

        'recouvrement_1': recouvrement_1,
        'recouvrement_2': recouvrement_2,
        'recouvrement_3': recouvrement_3,
        'recouvrement_4': recouvrement_4,
        'recouvrement_5': recouvrement_5,
        'recouvrement_6': recouvrement_6,
        'recouvrement_7': recouvrement_7,
        'recouvrement_8': recouvrement_8,
        'recouvrement_9': recouvrement_9,

        'renouvellement_1': renouvellement_1,
        'renouvellement_2': renouvellement_2,
        'renouvellement_3': renouvellement_3,
        'renouvellement_4': renouvellement_4,
        'renouvellement_5': renouvellement_5,
        'renouvellement_6': renouvellement_6,
        'renouvellement_7': renouvellement_7,
        'renouvellement_8': renouvellement_8,
        'renouvellement_9': renouvellement_9,

        'compte_dormant__1': compte_dormant__1,
        'compte_dormant__2': compte_dormant__2,
        'compte_dormant__3': compte_dormant__3,
        'compte_dormant__4': compte_dormant__4,
        'compte_dormant__5': compte_dormant__5,
        'compte_dormant__6': compte_dormant__6,
        'compte_dormant__7': compte_dormant__7,
        'compte_dormant__8': compte_dormant__8,
        'compte_dormant__9': compte_dormant__9,

    }
    template_name = 'pages/dashboard/dashboard_admin_view.html'
    return render(request, template_name, context)

