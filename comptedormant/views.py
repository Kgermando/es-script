from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages  # for message
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from comptedormant.models import Compte_dormant
from comptedormant.forms import Compte_dormantForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def compte_dormant_add(request):
    """
        Fonction Add new object
    """
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Compte_dormantForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            compte_dormant = form.save(commit=False)
            compte_dormant.user = request.user
            compte_dormant.save()
            messages.success(request, "Compte dormant enregistrée!")
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('compte_dormant:compte_dormant_list'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = Compte_dormantForm()
    context = {
        'form': form
    }
    template_name = 'pages/compte_dormant/compte_dormant_add.html'
    return render(request, template_name, context)



@login_required(login_url='/accounts/login/')
def compte_dormant_list(request): 
    """
        Fonction List objects
    """ 
    user = request.user
    compte_dormant_count = Compte_dormant.objects.filter(user=user).order_by('-created_date').count()
    compte_dormant = Compte_dormant.objects.filter(user=user).order_by('-created_date')
    paginator = Paginator(compte_dormant, 10)
    page = request.GET.get('page')
    try:
        compte_dormant_list = paginator.page(page)
    except PageNotAnInteger:
        compte_dormant_list = paginator.page(1)
    except EmptyPage:
        compte_dormant_list = paginator.page(paginator.num_pages)
    context = {
        'compte_dormant_list': compte_dormant_list,
        'compte_dormant_count': compte_dormant_count
    }  
    template_name = 'pages/compte_dormant/compte_dormant_list.html'
    return render(request, template_name, context)



@login_required(login_url='/accounts/login/')
def compte_dormant_view(request, id):  
    """
        Fonction Detail
    """
    user = request.user
    compte_dormant = Compte_dormant.objects.filter(user=user).get(id=id)
    context = {
        'compte_dormant': compte_dormant,
    }
    template_name = 'pages/compte_dormant/compte_dormant_view.html'
    return render(request, template_name, context)   



@login_required(login_url='/accounts/login/')
def compte_dormant_update(request, id):
    """
        Fonction de Mis à jour
    """
    compte_dormant = Compte_dormant.objects.get(id=id)
    form = DatForm(request.POST, instance=Compte_dormant)
    if form.is_valid():  
        form.user = request.user
        form.save()  
        messages.success(request, "Compte dormant modifié!")
        return redirect('compte_dormant:compte_dormant_list') 

    context = {
        'compte_dormant': compte_dormant,
        'form': form
    }  
    template_name = 'pages/compte_dormant/compte_dormant_update.html'
    return render(request, template_name, context)   



@login_required(login_url='/accounts/login/')
def compte_dormant_destroy(request, id):
    """
        Fonction de Suppresion
    """
    user = request.user
    compte_dormant = Compte_dormant.objects.filter(user=user).get(id=id)  
    compte_dormant.delete()  
    return redirect("compte_dormant:compte_dormant_list")  

