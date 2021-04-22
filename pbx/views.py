from django.shortcuts import render

from pbx.models import Cdr, Cel
# Create your views here.
def cdr_view(request):
     """
          CDR LIst
     """
     user = request.user
     cdr_list = Cdr.objects.filter(src=user).order_by('-calldate')[:10]
     # cdr_list = Cdr.objects.all()

     context = {
          'cdr_list': cdr_list
     }
     template_name = 'pages/pbx/cdr/cdr_list.html'
     return render(request, template_name, context)


def cdr_detail(request, uniqueid):
     cdr = Cdr.objects.get(uniqueid=uniqueid)
     context = {
          'cdr': cdr
     }
     template_name = 'pages/pbx/cdr/cdr_detail.html'
     return render(request, template_name, context)


def cel_view(request):
     """
          CEL LIst
     """
     cel_list = Cel.objects.all()[:10]

     context = {
          'cel_list': cel_list
     }
     template_name = 'pages/pbx/cel/cel_list.html'
     return render(request, template_name, context)


def cel_detail(request, uniqueid):
     """
          CEL detail
     """
     cel = Cel.objects.get(uniqueid=uniqueid)

     context = {
          'cel': cel
     }
     template_name = 'pages/pbx/cel/cel_detail.html'
     return render(request, template_name, context)


