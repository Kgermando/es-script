from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def index_view(request):

    context = {}
    template_name = 'pages/app/index.html'
    return render(request, template_name, context)

