from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages  # for message
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from xhtml2pdf import pisa
import xlwt
import csv
import logging

from contacts.models import Contact
from contacts.forms import ContactForm
# Create your views here.
@login_required
def contact_view(request):

    # user = request.user
    contact = Contact.objects.all().order_by('-created_date')
    contact_count = Contact.objects.all().count()
    paginator = Paginator(contact, 10)
    page = request.GET.get('page')
    try:
        contact_list = paginator.page(page)
    except PageNotAnInteger:
        contact_list = paginator.page(1)
    except EmptyPage:
        contact_list = paginator.page(paginator.num_pages)

    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request, "Contact enregistrées!")
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('contacts:contact_view'))
        else:
            form = ContactForm()
    context = {
        'form': form,
        'contact_list': contact_list,
        'contact_count': contact_count
    }
    template_name = 'pages/contacts/contact_view.html'
    return render(request, template_name, context)


def kyc_view(request):
    formContact = ContactForm(request.POST)
    if request.method == 'POST':
        if formContact.is_valid():
            contact = formContact.save(commit=False)
            contact.user = request.user
            contact.save()
            # messages.success(request, "Contact enregistrées!")
            return JsonResponse({'contact': 'success'})
    #     else:
    #         formContact = ContactForm()
    # context = {
    #     'form': form,
    #     'formContact': formContact
    # }

def export_contact_xls(request):
    user = request.user
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="contact.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Contact')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nom', 'Post_Nom', 'Prenom', 'Numero', 'Rue', 'Quartier', 'Commune', 'Ville', 'Province', 'Téléphone 1', 'Téléphone 2', 
	'Téléphone 3', 'Email', 'Website', 'Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'Remarque']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Contact.objects.filter(user=user).values_list('Nom', 'Post_Nom', 'Prenom', 'Numero', 'Rue', 'Quartier', 'Commune', 'Ville', 'Province', 'phonenumber', 'Tel2', 'Tel3',
            'Email', 'Website', 'Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'Remarque')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_contact_csv(request):
    user = request.user
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contact.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nom', 'Post_Nom', 'Prenom', 'Numero', 'Rue', 'Quartier', 'Commune', 'Ville', 'Province', 'Téléphone 1', 'Téléphone 2', 
	'Téléphone 3', 'Email', 'Website', 'Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'Remarque'])

    rows = Contact.objects.filter(user=user).values_list('Nom', 'Post_Nom', 'Prenom', 'Numero', 'Rue', 'Quartier', 'Commune', 'Ville', 'Province', 'phonenumber', 'Tel2', 'Tel3',
            'Email', 'Website', 'Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'Remarque')
    for row in rows:
        writer.writerow(row)

    return response



def export_contact_pdf(request):
	user = request.user
	template_path = 'pages/contacts/export_contact_pdf.html'
	contact_list = Contact.objects.filter(user=user)
	context = {
		'contact_list': contact_list
	}
	# Create a Django response object, and specify content_type as pdf
	response = HttpResponse(content_type='application/pdf')
	# If download
	response['Content-Disposition'] = 'attachment; filename="contacts.pdf"'

	# find the template and render it.
	template = get_template(template_path)
	html = template.render(context)

	# create a pdf
	pisa_status = pisa.CreatePDF(html, dest=response)
	# if error then show some funy view
	if pisa_status.err:
		return HttpResponse('We had some errors <pre>' + html + '</pre>')
	return response



@login_required
def upload_contact_csv(request):
    if 'GET' == request.method:
        csvdata = Contact.objects.all()
        context = {'csvdata': csvdata}
        return render(request, 'pages/contacts/upload_contact_csv.html', context)
    try:
        csv_file = request.FILES["csv_file"]

        if len(csv_file) == 0:
            messages.error(request, 'Empty File')
            return render(request, 'pages/contacts/upload_contact_csv.html')

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return render(request, 'pages/contacts/upload_contact_csv.html')

        if csv_file.multiple_chunks():
            messages.error(request, 'Uploaded file is too big (%.2f MB).' % (csv_file.size / (1000 * 1000),))
            return render(request, 'pages/contacts/upload_contact_csv.html')

        file_data = csv_file.read().decode("utf-8")

        lines = file_data.split("\n")
        for index, line in enumerate(lines):
            fields = line.split(",")
            if index == 0:
                if (fields[0] == 'created_date') and (fields[1] == 'Nom') and (fields[2] == 'Post_Nom') and (
                    fields[3] == 'Prenom') and (fields[4] == 'Numero') and (fields[5] == 'Rue') and (
                    fields[6] == 'Quartier') and (fields[7] == 'Commune') and (fields[8] == 'Ville') and (fields[9] == 'Province') and (
                    fields[10] == 'phonenumber') and (fields[11] == 'Tel2') and (fields[12] == 'Tel3') and (fields[13] == 'Email') and (
                    fields[14] == 'Website') and (fields[15] == 'Facebook') and (fields[16] == 'Instagram')  and (
                    fields[17] == 'Twitter')  and (fields[18] == 'LinkedIn')  and (fields[19] == 'Remarque') and (fields[20] == 'user'):
                    pass
                else:
                    messages.error(request, 'File is not Correct Headers')
                    return render(request, 'pages/contacts/upload_contact_csv.html')
                    break
            else:
                print(index)
                data = Contact(
                    created_date=fields[0],
                    Nom=fields[1],
                    Post_Nom=fields[2],
                    Prenom=fields[3],
                    Numero=fields[4],
                    Rue=fields[5],
                    Quartier=fields[6],
                    Commune=fields[7],
                    Ville=fields[8],
                    Province=fields[9],
                    phonenumber=fields[10],
                    Tel2=fields[11],
                    Tel3=fields[12],
                    Email=fields[13],
                    Website=fields[14],
                    Facebook=fields[15],
                    Instagram=fields[16],
                    Twitter=fields[17],
                    LinkedIn=fields[18],
                    Remarque=fields[19],
                    user=fields[20]
                )
                data.save()
        messages.success(request, "Successfully Uploaded CSV File")
        return redirect("contacts:contact_view")

    except Exception as e:
        messages.error(request, "Unable to upload file. " + e)
        return HttpResponseRedirect(reverse('contacts:contact_view'))
