from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import xlwt
import csv
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib import messages  # for message
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.forms.models import model_to_dict

import datetime
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4

from django.views.generic import View, DetailView
from scripting.utils import render_to_pdf
from django.template.loader import get_template
 
from dat.models import Dat
from dat.forms import DatForm

from contacts.models import Contact
from contacts.forms import ContactForm

# Create your views here.
@login_required
def dat_add(request):
    """
        Fonction Add new object
    """
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DatForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            dat = form.save(commit=False)
            dat.user = request.user
            dat.save()
            messages.success(request, "DAT enregistrée!")
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('dat:dat_list'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = DatForm()

    
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

        template_name = 'pages/dat/dat_add.html'
        return render(request, template_name, context)


@login_required
def dat_list(request): 
    """
        Fonction List objects
    """ 
    user = request.user
    dat_count = Dat.objects.filter(user=user).order_by('-created_date').count()
    dat = Dat.objects.filter(user=user).order_by('-created_date')
    paginator = Paginator(dat, 10)
    page = request.GET.get('page')
    

    try:
        dat_list = paginator.page(page)
    except PageNotAnInteger:
        dat_list = paginator.page(1)
    except EmptyPage:
        dat_list = paginator.page(paginator.num_pages)

    context = {
        'dat_list': dat_list,
        'dat_count': dat_count,
    }  
    template_name = 'pages/dat/dat_list.html'
    return render(request, template_name, context)    



@login_required
def dat_view(request, id):  
    """
        Fonction Detail
    """
    user = request.user
    dat = Dat.objects.filter(user=user).get(id=id)
    context = {
        'dat': dat,
    }  
    template_name = 'pages/dat/dat_view.html'
    return render(request, template_name, context)   



@login_required
def dat_update(request, id):
    """
        Fonction de Mis à jour
    """
    dat = Dat.objects.get(id=id)  
    form = DatForm(request.POST, instance=dat)  
    if form.is_valid():  
        form.user = request.user
        form.save()  
        messages.success(request, "DAT modifié!")
        return redirect('dat:dat_list') 

    context = {
        'dat': dat,
        'form': form
    }  
    template_name = 'pages/dat/dat_update.html'
    return render(request, template_name, context)   



@login_required
def dat_destroy(request, id):
    """
        Fonction de Suppresion
    """
    user = request.user
    dat = Dat.objects.filter(user=user).get(id=id)  
    dat.delete()  
    return redirect("dat:dat_list")  



def export_dat_xls(request):
    user = request.user
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="dat.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Dat')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['questions1', 'questions2', 'Contact', 'Statut', 'Bound', 'Agent',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Dat.objects.filter(user=user).values_list(
        'questions1', 'questions2', 'Contact',  'Statut', 'Bound', 'user')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



def export_dat_csv(request):
    user = request.user
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dat.csv"'

    writer = csv.writer(response)
    writer.writerow(['created_date', 'questions1', 'questions2',  'Statut', 'Bound', 'Contact', 'Agent', ])

    dat = Dat.objects.filter(user=user).values_list('created_date', 'questions1', 'questions2', 'Statut', 'Bound', 'Contact', 'user')
    for dat in dat:
        writer.writerow(dat)

    return response



# def export_dat_pdf(request):
#     response = HttpResponse(content_type='application/pdf')
#     d = datetime.date.today().strftime('%d-%m-%Y')
#     response['Content-Disposition'] = f'inline; filename="{d}pdf"'

#     buffer = BytesIO()
#     p = canvas.Canvas(buffer, pagesize=A4)

#     # Data
#     user = request.user
#     dat_count = Dat.objects.filter(user=user).order_by('-created_date').count()
#     dat = Dat.objects.filter(user=user).order_by('-created_date')
#     data = {
#         'dat': dat,
#         'dat_count': dat_count
#     } 

#     # Start writting the PDF here
#     p.setFont("Helvetica", 15, leading=None)
#     p.setFillColorRGB(0.29296875,0.453125,0.609375)
#     p.drawString(260,800, "Dat")
#     p.line(0,780,1000,780)
#     p.line(0,778,1000,778)
#     xl = 20
#     yl = 750
#     # Render data
#     for k,v in data.items():
#         p.setFont("Helvetica",15,leading=None)
#         p.drawString(xl,yl-12,f"{k}")
#         for value in v:
#             for key, val in value.items():
#                 p.setFont("Helvetica",10,leading=None) 
#                 p.drawString(xl,yl-20,f"{key} - {val}")
#                 yl = yl-60
    
#     p.setTitle(f'Report on {d}')
#     p.showPage()
#     p.save()

#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)

#     return response


# class Export_Dat_pdf(View):
#     def get(self, request, *args, **kwargs):
#         dat_count = Dat.objects.filter(user=request.user).order_by('-created_date').count()
#         dat = Dat.objects.filter(user=request.user).order_by('-created_date')
#         template = get_template('pages/dat/dat_pdf.html')
#         context = {
#             'dat': dat,
#             'dat_count': dat_count
#         }
#         html = template.render(context)
#         pdf = render_to_pdf('pages/dat/dat_pdf.html', context)
#         if pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             d = datetime.date.today().strftime('%d-%m-%Y')
#             filename = "dat%s.pdf" %(d)
#             content = "inline; filename='%s'" %(filename)
#             download = request.GET.get("download")
#             if download:
#                 content = "attachment; filename='%s'" %(filename)
#             response['Content-Disposition'] = content
#             return response
#         return HttpResponse("Not found")


class Export_Dat_pdf_List(View):
    """
        For list to pdf to based function
    """
    model = Dat
    def get(self, request, *args, **kwargs):
        dat = Dat.objects.filter(user=request.user).order_by('-created_date')
        data = {
            'dat': dat
            # 'today': datetime.date.today(), 
        }
        pdf = render_to_pdf('pages/dat/dat_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class Export_Dat_pdf(DetailView):
    """
        For detail to pdf based function
    """
    model = Dat
    def get(self, request, *args, **kwargs):
        dat = Dat.objects.get(id=self.kwargs.get('id'))
        data = {
            'dat': dat,
            # 'today': datetime.date.today(), 
        }
        pdf = render_to_pdf('pages/dat/dat_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

