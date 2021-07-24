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

from django.views.generic import DetailView
from scripting.utils import render_to_pdf

from acquisition.models import Acquisition
from acquisition.forms import AcquisitionForm

from contacts.models import Contact
from contacts.forms import ContactForm
# Create your views here.
@login_required
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
        template_name = 'pages/acquisition/acquisition_add.html'
        return render(request, template_name, context)



@login_required
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



@login_required
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



@login_required
def acquisition_update(request, id):
    """
        Fonction de Mis à jour
    """
    acquisition = Acquisition.objects.get(id=id)
    form = AcquisitionForm(request.POST, instance=acquisition)  
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



@login_required
def acquisition_destroy(request, id):
    """
        Fonction de Suppresion
    """
    user = request.user
    acquisition = Acquisition.objects.filter(user=user).get(id=id)  
    acquisition.delete()  
    return redirect("acquisition:acquisition_list")  


def export_acquisition_xls(request):
    user = request.user
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="acquisition.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Acquisition')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['user', 'questions1', 'questions3', 'questions4', 'questions5', 'questions6', 'Contact', 'Statut' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Acquisition.objects.filter(user=user).values_list(
        'user', 'questions1', 'questions3', 'questions4', 'questions5', 'questions6', 'Contact', 'Statut')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_acquisition_csv(request):
    user = request.user
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="acquisition.csv"'

    writer = csv.writer(response)
    writer.writerow(['user', 'created_date', 'questions1', 'questions3', 'questions4', 'questions5', 'questions6', 'Contact', 'Statut' ])

    acquisition = Acquisition.objects.filter(user=user).values_list(
        'user', 'created_date', 'questions1', 'questions3', 'questions4', 'questions5', 'questions6', 'Contact', 'Statut')
    for acquisition in acquisition:
        writer.writerow(acquisition)

    return response


class Export_Acquisition_pdf(DetailView):
    """
        For detail to pdf based function
    """
    model = Acquisition
    def get(self, request, *args, **kwargs):
        acquisition = Acquisition.objects.get(id=self.kwargs.get('id'))
        data = {
            'acquisition': acquisition,
            # 'today': datetime.date.today(), 
        }
        pdf = render_to_pdf('pages/acquisition/acquisition_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')