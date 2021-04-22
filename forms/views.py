from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages  # for message
from django.urls import reverse

from forms.forms import KycForm
# Create your views here.
def forms_view(request):

    form = KycForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            scripting = form.save(commit=False)
            scripting.user = request.user
            scripting.save()
            messages.success(request, "Questions enregistrées!")
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('forms:scripting_form'))
        else:
            form = KycForm()
    context = {
        'form': form,
    }
    template_name = 'pages/forms/forms_view.html'
    return render(request, template_name, context)


def produits_view(request):

    context = {}
    template_name = 'pages/forms/produits_view.html'
    return render(request, template_name, context)


def enquetes_view(request):

    context = {}
    template_name = 'pages/forms/enquetes_view.html'
    return render(request, template_name, context)
