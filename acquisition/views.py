from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages  # for message
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from acquisition.models import Acquisition
from acquisition.forms import AcquisitionForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def acquisition_add(request):
    """
        Fonction Add new object
    """
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AcquisitionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            acquisition = form.save(commit=False)
            acquisition.user = request.user
            acquisition.save()
            messages.success(request, "Acquisition enregistrée!")
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('acquisition:acquisition_list'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AcquisitionForm()
    context = {
        'form': form
    }
    template_name = 'pages/acquisition/acquisition_add.html'
    return render(request, template_name, context)



@login_required(login_url='/accounts/login/')
def acquisition_list(request): 
    """
        Fonction List objects
    """ 
    user = request.user
    acquisition_count = Acquisition.objects.filter(user=user).order_by('-created_date').count()
    acquisition = Acquisition.objects.filter(user=user).order_by('-created_date')
    paginator = Paginator(acquisition, 10)
    page = request.GET.get('page')
    try:
        acquisition_list = paginator.page(page)
    except PageNotAnInteger:
        acquisition_list = paginator.page(1)
    except EmptyPage:
        acquisition_list = paginator.page(paginator.num_pages)

    context = {
        'acquisition_list': acquisition_list,
        'acquisition_count': acquisition_count
    }  
    template_name = 'pages/acquisition/acquisition_list.html'
    return render(request, template_name, context)    



@login_required(login_url='/accounts/login/')
def acquisition_view(request, id):  
    """
        Fonction Detail
    """
    user = request.user
    acquisition = Acquisition.objects.filter(user=user).get(id=id)
    context = {
        'acquisition': acquisition,
    }  
    template_name = 'pages/acquisition/acquisition_view.html'
    return render(request, template_name, context)   



@login_required(login_url='/accounts/login/')
def acquisition_update(request, id):
    """
        Fonction de Mis à jour
    """
    acquisition = Acquisition.objects.get(id=id)
    form = DatForm(request.POST, instance=dat)  
    if form.is_valid():  
        form.user = request.user
        form.save()  
        messages.success(request, "Acquisition modifié!")
        return redirect('acquisition:acquisition_list') 

    context = {
        'acquisition': acquisition,
        'form': form
    }  
    template_name = 'pages/acquisition/acquisition_update.html'
    return render(request, template_name, context)   



@login_required(login_url='/accounts/login/')
def acquisition_destroy(request, id):
    """
        Fonction de Suppresion
    """
    user = request.user
    acquisition = Acquisition.objects.filter(user=user).get(id=id)  
    acquisition.delete()  
    return redirect("acquisition:acquisition_list")  

