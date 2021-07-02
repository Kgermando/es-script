from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages  # for message
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
import xlwt
import csv
from django.forms.models import model_to_dict

from renouvellement.models import Renouvellement
from renouvellement.forms import RenouvellementForm

from contacts.models import Contact
from contacts.forms import ContactForm

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
    form = RenouvellementForm(request.POST, instance=renouvellement)
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




def export_renouvellement_xls(request):
    user = request.user
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="renouvellement.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Renouvellement')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['id', 'questions1', 'questions2', 'questions3', 'questions4', 'questions5', 'questions6', 'questions7', 'questions8', 'questions9',
        'questions10', 'questions12', 'questions13', 'questions15', 'questions16', 'Q19temps_a_contacter',
        'montant_de_pret', 'duree_de_credit', 'montant_a_rembourser_chaque_mois', 'montant_des_ventes_bonne_journee',
        'montant_des_ventes_mauvaise_journee', 'date_a_laquelle_recevoir_credit', 'Nom_du_garant', 'Activite',
        'Commentaire', 'Concurrent', 'CommentaireQ17', 'Statut',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Renouvellement.objects.filter(user=user).values_list(
        'id', 'questions1', 'questions2', 'questions3', 'questions4', 'questions5', 'questions6', 'questions7', 'questions8', 'questions9',
        'questions10', 'questions12', 'questions13', 'questions15', 'questions16', 'Q19temps_a_contacter',
        'montant_de_pret', 'duree_de_credit', 'montant_a_rembourser_chaque_mois', 'montant_des_ventes_bonne_journee',
        'montant_des_ventes_mauvaise_journee', 'date_a_laquelle_recevoir_credit', 'Nom_du_garant', 'Activite',
        'Commentaire', 'Concurrent', 'CommentaireQ17', 'Statut',)
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



def export_renouvellement_csv(request):
    user = request.user
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dat.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'questions1', 'questions2', 'questions3', 'questions4', 'questions5', 'questions6', 'questions7', 'questions8', 'questions9',
        'questions10', 'questions12', 'questions13', 'questions15', 'questions16', 'Q19temps_a_contacter',
        'montant_de_pret', 'duree_de_credit', 'montant_a_rembourser_chaque_mois', 'montant_des_ventes_bonne_journee',
        'montant_des_ventes_mauvaise_journee', 'date_a_laquelle_recevoir_credit', 'Nom_du_garant', 'Activite',
        'Commentaire', 'Concurrent', 'CommentaireQ17', 'Statut',])

    renouvellement = Renouvellement.objects.filter(user=user).values_list('id', 'questions1', 'questions2', 'questions3', 'questions4', 'questions5', 'questions6', 'questions7', 'questions8', 'questions9',
        'questions10', 'questions12', 'questions13', 'questions15', 'questions16', 'Q19temps_a_contacter',
        'montant_de_pret', 'duree_de_credit', 'montant_a_rembourser_chaque_mois', 'montant_des_ventes_bonne_journee',
        'montant_des_ventes_mauvaise_journee', 'date_a_laquelle_recevoir_credit', 'Nom_du_garant', 'Activite',
        'Commentaire', 'Concurrent', 'CommentaireQ17', 'Statut',)
    for renouvellement in renouvellement:
        writer.writerow(renouvellement)

    return response
