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

from recouvrement.models import Recouvrement
from recouvrement.forms import RecouvrementForm

from contacts.models import Contact
from contacts.forms import ContactForm

# Create your views here.
@login_required
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
        template_name = 'pages/recouvrement/recouvrement_add.html'
        return render(request, template_name, context)



@login_required
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



@login_required
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



@login_required
def recouvrement_update(request, id):
    """
        Fonction de Mis à jour
    """
    recouvrement = Recouvrement.objects.get(id=id)  
    form = RecouvrementForm(request.POST, instance=recouvrement)  
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



@login_required
def recouvrement_destroy(request, id):
    """
        Fonction de Suppresion
    """
    user = request.user
    recouvrement = Recouvrement.objects.filter(user=user).get(id=id)  
    recouvrement.delete()  
    return redirect("recouvrement:recouvrement_list")  




def export_recouvrement_xls(request):
    user = request.user
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="recouvrement.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('recouvrement')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['user', 'questions1', 'questions2', 'Statut', 'Bound', 'Contact']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Recouvrement.objects.filter(user=user).values_list(
        'user', 'questions1', 'questions2', 'Statut', 'Bound', 'Contact')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_recouvrement_csv(request):
    user = request.user
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="recouvrement.csv"'

    writer = csv.writer(response)
    writer.writerow(['user', 'created_date', 'questions1', 'questions2', 'Statut', 'Bound', 'Contact'])

    recouvrement = Recouvrement.objects.filter(user=user).values_list('user', 'created_date', 'questions1', 'questions2', 'Statut', 'Bound', 'Contact')
    for recouvrement in recouvrement:
        writer.writerow(recouvrement)

    return response
