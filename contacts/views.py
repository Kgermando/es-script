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

    user = request.user
    contact = Contact.objects.filter(user=user).order_by('-created_date')
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
        'contact_list': contact_list
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



@login_required
def upload_contact_csv(request):
	data = {}
	if "GET" == request.method:
		return render(request, "pages/contacts/upload_contact_csv.html", data)
    # if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("contacts:upload_contact_csv"))
    # if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
			return HttpResponseRedirect(reverse("contacts:upload_contact_csv"))

		file_data = csv_file.read().decode("utf-8")		
 
		lines = file_data.split("\n")
		# loop over the lines and save them in db. If error , store as string and then display
		for line in lines:						
			fields = line.split(",")
			data_dict = {"Nom", "Post_Nom", "Prenom", "Numero", "Quartier", "Commune", "Province", "Pays", "Tel1", "Tel2", "Email",
                     "Website", "Facebook", "Instagram", "Twitter", "LinkedIn", "Remarque", "user", "created_date"}
			# data_dict["Nom"] = fields[0]
			# data_dict["Post_Nom"] = fields[1]
			# data_dict["Prenom"] = fields[2]
			# data_dict["Numero"] = fields[3]
			try:
				form = Contact(data_dict)
				if form.is_valid():
					form.save()	
					return HttpResponseRedirect(reverse("contacts:contact_view"))				
				else:
					logging.getLogger("error_logger").error(form.errors.as_json())												
			except Exception as e:
				logging.getLogger("error_logger").error(repr(e))					
				pass

	except Exception as e:
		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		messages.error(request,"Unable to upload file. "+repr(e))
 
	return HttpResponseRedirect(reverse("contacts:upload_contact_csv"))



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

    rows = Contact.objects.filter(user=user).values_list('Nom', 'Post_Nom', 'Prenom', 'Numero', 'Rue', 'Quartier', 'Commune', 'Ville', 'Province', 'Tel1', 'Tel2', 'Tel3',
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

    rows = Contact.objects.filter(user=user).values_list('Nom', 'Post_Nom', 'Prenom', 'Numero', 'Rue', 'Quartier', 'Commune', 'Ville', 'Province', 'Tel1', 'Tel2', 'Tel3',
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
