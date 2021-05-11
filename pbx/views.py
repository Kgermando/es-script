from django.shortcuts import render
from datetime import timedelta, datetime, date, time as datetime_time
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required

from pbx.models import Cdr, Cel
from pbx.forms import ReportFilterForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def cdr_view(request):
     """
          CDR LIst
     """
     user = request.user.username
     cdr = Cdr.objects.filter(src=user).order_by('-calldate')[:10]
     # cdr_list = Cdr.objects.all()
     paginator = Paginator(cdr, 10)
     page = request.GET.get('page')
     try:
          cdr_list = paginator.page(page)
     except PageNotAnInteger:
          cdr_list = paginator.page(1)
     except EmptyPage:
          cdr_list = paginator.page(paginator.num_pages)

     context = {
          'cdr_list': cdr_list
     }
     template_name = 'pages/pbx/cdr/cdr_list.html'
     return render(request, template_name, context)

@login_required(login_url='/accounts/login/')
def cdr_detail(request, uniqueid):
     cdr = Cdr.objects.get(uniqueid=uniqueid)
     context = {
          'cdr': cdr
     }
     template_name = 'pages/pbx/cdr/cdr_detail.html'
     return render(request, template_name, context)

@login_required(login_url='/accounts/login/')
def cel_view(request):
     """
          CEL LIst
     """
     user = request.user
     cel = Cel.objects.filter(cid_num=user).order_by('-eventtime')[:10]
     paginator = Paginator(cel, 10)
     page = request.GET.get('page')
     try:
          cel_list = paginator.page(page)
     except PageNotAnInteger:
          cel_list = paginator.page(1)
     except EmptyPage:
          cel_list = paginator.page(paginator.num_pages)

     context = {
          'cel_list': cel_list
     }
     template_name = 'pages/pbx/cel/cel_list.html'
     return render(request, template_name, context)

@login_required(login_url='/accounts/login/')
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

