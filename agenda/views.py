from datetime import datetime, date
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages  # for message
from django.urls import reverse

from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta
import calendar
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from agenda.models import Note
from agenda.forms import NoteForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def agenda_view(request):

    context = {}
    template_name = 'pages/agendas/agenda_view.html'
    return render(request, template_name, context)

@login_required(login_url='/accounts/login/')
def agenda_detail(request, agenda_id):

    context = {}
    template_name = 'pages/agendas/agenda_detail.html'
    return render(request, template_name, context)

@login_required(login_url='/accounts/login/')
def note_view(request):
    user  = request.user
    form = NoteForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, "Note enregistrée!")
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('agenda:note_view'))
        else:
            form = NoteForm()

    note_list = Note.objects.filter(user=user).order_by('-created_date')
    
    context = {
        'form': form,
        'note_list': note_list,
    }
    template_name = 'pages/agendas/note_view.html'
    return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def note_detail(request, id):
    note = Note.objects.get(id=id)

    context = {
        'note': note
    }
    template_name = 'pages/agendas/note_detail.html'
    return render(request, template_name, context)


class NoteDeleteView(generic.DeleteView):
    model = Note
    login_url = '/accounts/login/'
    template_name = 'pages/agendas/remove_note.html'
    success_url = reverse_lazy('agenda:note_view')

