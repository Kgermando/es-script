from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages  # for message
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from commprom.models import Commprom
from commprom.forms import CommpromForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def commprom_add(request):  
    """
        Fonction Add new object
    """
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommpromForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            commprom = form.save(commit=False)
            commprom.user = request.user
            commprom.save()
            messages.success(request, "Communication-Promotion enregistrée!")
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('commprom:commprom_list'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CommpromForm()
    context = {
        'form': form
    }
    template_name = 'pages/commprom/commprom_add.html'
    return render(request, template_name, context)  


@login_required(login_url='/accounts/login/')
def commprom_list(request): 
    """
        Fonction List objects
    """ 
    user = request.user
    commprom_count = Commprom.objects.filter(user=user).order_by('-created_date').count()
    commprom = Commprom.objects.filter(user=user).order_by('-created_date')
    paginator = Paginator(commprom, 10)
    page = request.GET.get('page')
    try:
        commprom_list = paginator.page(page)
    except PageNotAnInteger:
        commprom_list = paginator.page(1)
    except EmptyPage:
        commprom_list = paginator.page(paginator.num_pages)

    context = {
        'commprom_list': commprom_list,
        'commprom_count': commprom_count,
    }  
    template_name = 'pages/commprom/commprom_list.html'
    return render(request, template_name, context)    



@login_required(login_url='/accounts/login/')
def commprom_view(request, id):  
    """
        Fonction Detail
    """
    user = request.user
    commprom = Commprom.objects.filter(user=user).get(id=id)
    context = {
        'commprom': commprom,
    }  
    template_name = 'pages/commprom/commprom_view.html'
    return render(request, template_name, context)   



@login_required(login_url='/accounts/login/')
def commprom_update(request, id):
    """
        Fonction de Mis à jour
    """
    commprom = Commprom.objects.get(id=id)  
    form = CommpromForm(request.POST, instance=commprom)  
    if form.is_valid():  
        form.user = request.user
        form.save()  
        messages.success(request, "Commerciale et promotion Modifié!")
        return redirect('commprom:commprom_list')

    context = {
        'commprom': commprom,
    }  
    template_name = 'pages/commprom/commprom_update.html'
    return render(request, template_name, context)   



@login_required(login_url='/accounts/login/')
def commprom_destroy(request, id):
    """
        Fonction de Suppresion
    """
    user = request.user
    commprom = Commprom.objects.filter(user=user).get(id=id)  
    commprom.delete()  
    return redirect("commprom:commprom_list")  

