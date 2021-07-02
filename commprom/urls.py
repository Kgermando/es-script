
from django.urls import path

from commprom.views import (commprom_add, 

        commprom_list, commprom_update, commprom_view, commprom_destroy, export_commprom_xls, export_commprom_csv)

app_name= 'commprom'

urlpatterns = [
    path('commprom_add/', commprom_add, name='commprom_add'),
    path('commprom_list/', commprom_list, name='commprom_list'),
    path('commprom_update/<int:id>/', commprom_update, name='commprom_update'),
    path('commprom_view/<int:id>/', commprom_view, name='commprom_view'),
    path('commprom_destroy/<int:id>/', commprom_destroy, name='commprom_destroy'),
    path('export/xls/', export_commprom_xls, name='export_commprom_xls'),
    path('export/csv/', export_commprom_csv, name='export_commprom_csv'),
]
