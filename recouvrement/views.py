from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages  # for message
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from recouvrement.models import Recouvrement
from recouvrement.forms import RecouvrementForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def recouvrement_add(request):
    """
        Fonction Add new object
    """
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RecouvrementForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            recouvrement = form.save(commit=False)
            recouvrement.user = request.user
            recouvrement.save()
            messages.success(request, "Recouvrement enregistrée!")
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('recouvrement:recouvrement_list'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RecouvrementForm()
    context = {
        'form': form
    }
    template_name = 'pages/recouvrement/recouvrement_add.html'
    return render(request, template_name, context)



@login_required(login_url='/accounts/login/')
def recouvrement_list(request): 
    """
        Fonction List objects
    """ 
    user = request.user
    commprom_count = Recouvrement.objects.filter(user=user).order_by('-created_date').count
    recouvrement = Recouvrement.objects.filter(user=user).order_by('-created_date')
    paginator = Paginator(recouvrement, 10)
    page = request.GET.get('page')
    try:
        recouvrement_list = paginator.page(page)
    except PageNotAnInteger:
        recouvrement_list = paginator.page(1)
    except EmptyPage:
        recouvrement_list = paginator.page(paginator.num_pages)

    context = {
        'recouvrement_list': recouvrement_list,
        'commprom_count': commprom_count,
    }  
    template_name = 'pages/recouvrement/recouvrement_list.html'
    return render(request, template_name, context)    



@login_required(login_url='/accounts/login/')
def recouvrement_view(request, id):  
    """
        Fonction Detail
    """
    user = request.user
    recouvrement = Recouvrement.objects.filter(user=user).get(id=id)
    context = {
        'recouvrement': recouvrement,
    }  
    template_name = 'pages/recouvrement/recouvrement_view.html'
    return render(request, template_name, context)   



@login_required(login_url='/accounts/login/')
def recouvrement_update(request, id):
    """
        Fonction de Mis à jour
    """
    recouvrement = Recouvrement.objects.get(id=id)  
    form = RecouvrementForm(request.POST, instance=dat)  
    if form.is_valid():  
        form.user = request.user
        form.save()  
        messages.success(request, "Recouvrement modifié!")
        return redirect('recouvrement:recouvrement_list') 

    context = {
        'recouvrement': recouvrement,
        'form': form
    }  
    template_name = 'pages/recouvrement/recouvrement_update.html'
    return render(request, template_name, context)   



@login_required(login_url='/accounts/login/')
def recouvrement_destroy(request, id):
    """
        Fonction de Suppresion
    """
    user = request.user
    recouvrement = Recouvrement.objects.filter(user=user).get(id=id)  
    recouvrement.delete()  
    return redirect("recouvrement:recouvrement_list")  

