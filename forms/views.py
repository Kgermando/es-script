from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages  # for message
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from forms.models import Kyc, Contact
from forms.forms import KycForm, ContactForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def scripting_forms(request):

    form = KycForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            scripting = form.save(commit=False)
            scripting.user = request.user
            scripting.save()
            messages.success(request, "Scripting enregistrées!")
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('forms:scripting_list'))
        else:
            form = KycForm()
    context = {
        'form': form,
    }
    template_name = 'pages/forms/forms_view.html'
    return render(request, template_name, context)

@login_required(login_url='/accounts/login/')
def scripting_forms_edit(request, id):
    scripting = Kyc.objects.get(id=id)
    form = KycForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            scripting = form.save(commit=False)
            scripting.user = request.user
            scripting.save()
            messages.success(request, "Scripting modifié!")
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('forms:scripting_list'))
        else:
            form = KycForm()
    context = {
        'form': form,
        'scripting': scripting,
    }
    template_name = 'pages/forms/scripting_forms_edit.html'
    return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def scripting_list(request):

    user = request.user
    kyc = Kyc.objects.filter(user=user).order_by('-created_date')
    paginator = Paginator(kyc, 10)
    page = request.GET.get('page')
    try:
        kyc_list = paginator.page(page)
    except PageNotAnInteger:
        kyc_list = paginator.page(1)
    except EmptyPage:
        kyc_list = paginator.page(paginator.num_pages) 

    context = {
        'kyc_list': kyc_list,
    }
    template_name = 'pages/forms/scripting_list.html'
    return render(request, template_name, context)

@login_required(login_url='/accounts/login/')
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
            return HttpResponseRedirect(reverse('forms:contact_view'))
        else:
            form = ContactForm()


    context = {
        'form': form,
        'contact_list': contact_list
    }
    template_name = 'pages/forms/contact_view.html'
    return render(request, template_name, context)

@login_required(login_url='/accounts/login/')
def upload_csv(request):
	data = {}
	if "GET" == request.method:
		return render(request, "pages/forms/upload_csv.html", data)
    # if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("forms:upload_csv"))
    # if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
			return HttpResponseRedirect(reverse("forms:upload_csv"))

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
				else:
					logging.getLogger("error_logger").error(form.errors.as_json())												
			except Exception as e:
				logging.getLogger("error_logger").error(repr(e))					
				pass

	except Exception as e:
		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		messages.error(request,"Unable to upload file. "+repr(e))
 
	return HttpResponseRedirect(reverse("forms:upload_csv"))

@login_required(login_url='/accounts/login/')
def enquetes_view(request):

    context = {}
    template_name = 'pages/forms/enquetes_view.html'
    return render(request, template_name, context)


# class Dat()