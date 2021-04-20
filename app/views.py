from django.shortcuts import render

# Create your views here.
def index_view(request):

    context = {}
    template_name = 'pages/app/index.html'
    return render(request, template_name, context)

