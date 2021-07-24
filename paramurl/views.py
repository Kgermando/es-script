from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from acquisition.models import Acquisition
from contacts.models import Contact
from commprom.models import Commprom
from comptedormant.models import Compte_dormant
from dat.models import Dat
from recouvrement.models import Recouvrement
from renouvellement.models import Renouvellement
# Create your views here.

def paramurl_view(request):
    # Get value
    phonenumber = request.GET.get('phonenumber', None)
    campaignname = request.GET.get('campaignname', None)

    # Campaign
    dat = 'dat',
    commprom = 'commprom',
    comptedormant = 'comptedormant',
    acquisition = 'acquisition',
    recouvrement = 'recouvrement',
    renouvellement = 'renouvellement',

    # campaigns = [dat, commprom, comptedormant, acquisition, recouvrement, renouvellement]

    if campaignname is not None:
    
        try:
            phone = Contact.objects.get(phonenumber=phonenumber)

            if phone is not None:

                if campaignname in acquisition:
                    acquisition_campaign = Acquisition.objects.filter(Contact=phone).filter(campaignname=campaignname).first()
                    
                    context = {
                        'acquisition_campaign': acquisition_campaign
                    }
                    template_name = 'pages/param_url/param_acquisition.html'
                    return render(request, template_name, context)

                elif campaignname in commprom:
                    commprom_campaign = Commprom.objects.filter(Contact=phone).filter(campaignname=campaignname).first()
                    context= {
                        'commprom_campaign': commprom_campaign
                    }
                    template_name = 'pages/param_url/param_commprom.html'
                    return render(request, template_name, context)

                elif campaignname in comptedormant:
                    comptedormant_campaign = Compte_dormant.objects.filter(Contact=phone).filter(campaignname=campaignname).first()
                    context = {
                        'comptedormant_campaign': comptedormant_campaign
                    }
                    template_name = 'pages/param_url/param_comptedormant.html'
                    return render(request, template_name, context)
                
                elif campaignname in dat:
                    dat_campaign = Dat.objects.filter(Contact=phone).filter(campaignname=campaignname).first()
                    # return HttpResponse('<h1>Dat numero {} {} {} </h1>'.format(phone, dat_campaign.id, dat_campaign.Statut))
                    context= {
                        'dat_campaign': dat_campaign
                    }
                    template_name = 'pages/param_url/param_dat.html'
                    return render(request, template_name, context)

                elif campaignname in recouvrement:
                    recouvrement_campaign = Recouvrement.objects.filter(Contact=phone).filter(campaignname=campaignname).first()
                    context = {
                        'recouvrement_campaign': recouvrement_campaign
                    }
                    template_name = 'pages/param_url/param_recouvrement.html'
                    return render(request, template_name, context)

                elif campaignname in renouvellement:
                    renouvellement_campaign = Renouvellement.objects.filter(Contact=phone).filter(campaignname=campaignname).first()
                    context = {
                        'renouvellement_campaign': renouvellement_campaign
                    }
                    template_name = 'pages/param_url/param_renouvellement.html'
                    return render(request, template_name, context)
                
                # else:
                #     return HttpResponse('<h1>La campaign n\'est pas trouvé</h1>')
        
        except Contact.DoesNotExist:
            return HttpResponse('<h1>Le contact n\'existe pas</h1>')
    else:
        return HttpResponse('<h1>La campaign n\'existe pas</h1>')
