from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User

from pbx.models import Cdr, Cel
from agenda.models import Note
from forms.models import Contact
# Create your views here.
@login_required
def dashboard_view(request):
    user = request.user

    # report CDR 
    cdr_answered = Cdr.objects.filter(src=user).filter(lastapp='Dial').count()
    cdr_no_answer = Cdr.objects.filter(src=user).filter(lastapp='HangUp').count()
    cdr_answered_cout = Cdr.objects.all()
    cdr_no_answer_cout = Cdr.objects.filter(src=user).filter(lastapp='HangUp')
    cdr_total = Cdr.objects.filter(src=user).count()
    cdr_list = Cdr.objects.filter(src=user).order_by('-calldate')[:5]

    # Notes
    note_nbr = Note.objects.filter(user=user).order_by('-created_date').count()
    
    context = {
        'cdr_answered': cdr_answered,
        'cdr_no_answer': cdr_no_answer,
        'cdr_answered_cout' : cdr_answered_cout,
        'cdr_no_answer_cout': cdr_no_answer_cout,
        'cdr_total': cdr_total,
        'cdr_list': cdr_list,

        'note_nbr': note_nbr,
    }
    template_name = 'pages/dashboard/dashboard_view.html'
    return render(request, template_name, context)


def dashboard_admin_view(request):
    user = request.user
    user_list = User.objects.all().count()
    # report CDR 
    cdr_answered = Cdr.objects.all().filter(lastapp='Dial').count()
    cdr_no_answer = Cdr.objects.all().filter(lastapp='HangUp').count()
    cdr_total = Cdr.objects.all().count()
    cdr_list = Cdr.objects.all().order_by('-calldate')[:5]


    # Notes
    note_nbr = Note.objects.all().count()

    # Contacts
    contact_list = Contact.objects.all().count()
    
    context = {
        'user_list': user_list,
        'cdr_answered': cdr_answered,
        'cdr_no_answer': cdr_no_answer,
        'cdr_total': cdr_total,
        'cdr_list': cdr_list,

        'note_nbr': note_nbr,
        'contact_list': contact_list,
    }
    template_name = 'pages/dashboard/dashboard_admin_view.html'
    return render(request, template_name, context)

