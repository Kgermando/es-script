from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User


# Create your views here.
@login_required
def dashboard_view(request):

    context = {}
    template_name = 'pages/dashboard/dashboard_view.html'
    return render(request, template_name, context)
