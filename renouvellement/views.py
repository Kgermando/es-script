from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages  # for message
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from renouvellement.models import Renouvellement
from renouvellement.forms import RenouvellementForm

# Create your views here.
@login_required
def renouvellement_add(request):
    """
        Fonction Add new object
    """
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RenouvellementForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            renouvellement = form.save(commit=False)
            renouvellement.user = request.user
            renouvellement.save()
            messages.success(request, "Renouvellement de crédit enregistrée!")
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('renouvellement:renouvellement_list'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RenouvellementForm()
    context = {
        'form': form
    }
    template_name = 'pages/renouvellement/renouvellement_add.html'
    return render(request, template_name, context)



@login_required
def renouvellement_list(request): 
    """
        Fonction List objects
    """ 
    user = request.user
    renouvellement_count = Renouvellement.objects.filter(user=user).order_by('-created_date').count()
    renouvellement = Renouvellement.objects.filter(user=user).order_by('-created_date')
    paginator = Paginator(renouvellement, 10)
    page = request.GET.get('page')
    try:
        renouvellement_list = paginator.page(page)
    except PageNotAnInteger:
        renouvellement_list = paginator.page(1)
    except EmptyPage:
        renouvellement_list = paginator.page(paginator.num_pages)

    context = {
        'renouvellement_list': renouvellement_list,
        'renouvellement_count': renouvellement_count
    }  
    template_name = 'pages/renouvellement/renouvellement_list.html'
    return render(request, template_name, context)    



@login_required
def renouvellement_view(request, id):  
    """
        Fonction Detail
    """
    user = request.user
    renouvellement = Renouvellement.objects.filter(user=user).get(id=id)
    context = {
        'renouvellement': renouvellement,
    }  
    template_name = 'pages/renouvellement/renouvellement_view.html'
    return render(request, template_name, context)   



@login_required
def renouvellement_update(request, id):
    """
        Fonction de Mis à jour
    """
    renouvellement = Renouvellement.objects.get(id=id)
    form = RenouvellementForm(request.POST, instance=dat)  
    if form.is_valid():  
        form.user = request.user
        form.save()  
        messages.success(request, "Renouvellement modifié!")
        return redirect('renouvellement:renouvellement_list') 

    context = {
        'renouvellement': renouvellement,
        'form': form
    }  
    template_name = 'pages/renouvellement/renouvellement_update.html'
    return render(request, template_name, context)   



@login_required
def renouvellement_destroy(request, id):
    """
        Fonction de Suppresion
    """
    user = request.user
    renouvellement = Renouvellement.objects.filter(user=user).get(id=id)  
    renouvellement.delete()  
    return redirect("renouvellement:renouvellement_list")  

