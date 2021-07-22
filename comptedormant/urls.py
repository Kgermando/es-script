
from django.urls import path

from comptedormant.views import (
    compte_dormant_add, 
    compte_dormant_list, compte_dormant_view, 
    compte_dormant_update, compte_dormant_destroy,
    export_compte_dormant_xls, export_compte_dormant_csv, Export_compte_dormant_pdf)

app_name = 'compte_dormant'

urlpatterns = [
    path('compte_dormant_add/', compte_dormant_add, name='compte_dormant_add'),
    path('compte_dormant_list/', compte_dormant_list, name='compte_dormant_list'),
    path('compte_dormant_update/<int:id>/', compte_dormant_update, name='compte_dormant_update'),
    path('compte_dormant_view/<int:id>/', compte_dormant_view, name='compte_dormant_view'),
    path('compte_dormant_destroy/<int:id>/', compte_dormant_destroy, name='compte_dormant_destroy'),
    path('export/xls/', export_compte_dormant_xls, name='export_compte_dormant_xls'),
    path('export/csv/', export_compte_dormant_csv, name='export_compte_dormant_csv'),
    path('export/pdf/<int:id>/',
         Export_compte_dormant_pdf.as_view(), name='export_compte_dormant_pdf'),
]
