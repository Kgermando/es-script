from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages  # for message
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.forms.models import model_to_dict
import xlwt
import csv

from contacts.models import Contact
from contacts.forms import ContactForm

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
    
    if request.method == 'POST':
        if request.is_ajax():
            formContact = ContactForm(request.POST)
            if formContact.is_valid():
                    formContact.cleaned_data
                    formContact.user = request.user
                    formContact.save()
                    latest = Contact.objects.latest('id').id
                    contact_object = model_to_dict(Contact.objects.get(pk=latest))  
                
                    return JsonResponse({'error': False, 'data': contact_object})
            else:
                    print(formContact.errors)
                    return JsonResponse({'error': True, 'data': formContact.errors})
        else:
                error = {
                    'message': 'Error, must be an Ajax call.'
                }
                return JsonResponse(error, content_type="application/json")
    else:
        formContact = ContactForm()

        context = {
            'form': form,
            'formContact': formContact
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
    form = ContactForm(request.POST, instance=Compte_dormant)
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



def export_compte_dormant_xls(request):
    user = request.user
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="compte_dormant.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Compte_dormant')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['user', 'questions1', 'questions2', 'questions3', 'questions4', 'Statut', 'Bound', 'Contact']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Compte_dormant.objects.filter(user=user).values_list(
        'user', 'questions1', 'questions2', 'questions3', 'questions4', 'Statut', 'Bound', 'Contact')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



def export_compte_dormant_csv(request):
    user = request.user
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="compte_dormant.csv"'

    writer = csv.writer(response)
    writer.writerow(['user', 'created_date', 'questions1', 'questions2', 'questions3', 'questions4', 'Statut', 'Bound', 'Contact'])

    compte_dormant = Compte_dormant.objects.filter(user=user).values_list('user', 'created_date', 'questions1', 'questions2', 'questions3', 'questions4', 'Statut', 'Bound', 'Contact')
    for compte_dormant in compte_dormant:
        writer.writerow(compte_dormant)

    return response

