from django.shortcuts import render

# Create your views here.
def forms_view(request):

    context = {}
    template_name = 'pages/forms/forms_view.html'
    return render(request, template_name, context)
