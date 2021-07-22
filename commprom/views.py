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

from django.views.generic import View, DetailView
from scripting.utils import render_to_pdf
from django.template.loader import get_template

from django.views.generic import DetailView
from scripting.utils import render_to_pdf

from contacts.models import Contact
from contacts.forms import ContactForm

from commprom.models import Commprom
from commprom.forms import CommpromForm
# Create your views here.
@login_required
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
        template_name = 'pages/commprom/commprom_add.html'
        return render(request, template_name, context)  


@login_required
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



@login_required
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



@login_required
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



@login_required
def commprom_destroy(request, id):
    """
        Fonction de Suppresion
    """
    user = request.user
    commprom = Commprom.objects.filter(user=user).get(id=id)  
    commprom.delete()  
    return redirect("commprom:commprom_list")  





def export_commprom_xls(request):
    user = request.user
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="commprom.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Commprom')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['user', 'questions1', 'questions2', 'Statut', 'Bound', 'Contact']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Commprom.objects.filter(user=user).values_list(
        'user', 'questions1', 'questions2', 'Statut', 'Bound', 'Contact')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



def export_commprom_csv(request):
    user = request.user
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="commprom.csv"'

    writer = csv.writer(response)
    writer.writerow(['user', 'created_date', 'questions1', 'questions2', 'Statut', 'Bound', 'Contact'])

    commprom = Commprom.objects.filter(user=user).values_list('user', 'created_date', 'questions1', 'questions2', 'Statut', 'Bound', 'Contact')
    for commprom in commprom:
        writer.writerow(commprom)

    return response



class Export_Commprom_pdf(DetailView):
    """
        For detail to pdf based function
    """
    model = Commprom
    def get(self, request, *args, **kwargs):
        commprom = Commprom.objects.get(id=self.kwargs.get('id'))
        data = {
            'commprom': commprom,
            # 'today': datetime.date.today(), 
        }
        pdf = render_to_pdf('pages/commprom/commprom_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')