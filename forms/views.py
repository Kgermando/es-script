from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages  # for message
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from forms.models import Kyc
from forms.forms import KycForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def scripting_forms(request):

    form = KycForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            scripting = form.save(commit=False)
            scripting.user = request.user
            scripting.save()
            messages.success(request, "Scripting enregistrées!")
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('forms:scripting_list'))
        else:
            form = KycForm()
    context = {
        'form': form,
    }
    template_name = 'pages/forms/forms_view.html'
    return render(request, template_name, context)

@login_required(login_url='/accounts/login/')
def scripting_forms_edit(request, id):
    scripting = Kyc.objects.get(id=id)
    form = KycForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            scripting = form.save(commit=False)
            scripting.user = request.user
            scripting.save()
            messages.success(request, "Scripting modifié!")
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('forms:scripting_list'))
        else:
            form = KycForm()
    context = {
        'form': form,
        'scripting': scripting,
    }
    template_name = 'pages/forms/scripting_forms_edit.html'
    return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def scripting_list(request):

    user = request.user
    kyc = Kyc.objects.filter(user=user).order_by('-created_date')
    paginator = Paginator(kyc, 10)
    page = request.GET.get('page')
    try:
        kyc_list = paginator.page(page)
    except PageNotAnInteger:
        kyc_list = paginator.page(1)
    except EmptyPage:
        kyc_list = paginator.page(paginator.num_pages) 

    context = {
        'kyc_list': kyc_list,
    }
    template_name = 'pages/forms/scripting_list.html'
    return render(request, template_name, context)



@login_required(login_url='/accounts/login/')
def enquetes_view(request):

    context = {}
    template_name = 'pages/forms/enquetes_view.html'
    return render(request, template_name, context)


# class Dat()