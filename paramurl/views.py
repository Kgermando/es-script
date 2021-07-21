 
from django.http import HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
def paramurl_view(request, phonenumber, campagain):

    try:
        phonenumber = request.GET.get('phonenumber')
        campagain = request.GET.get('campagain')
    except:
        return HttpResponseBadRequest
