
from django.urls import path

from renouvellement.views import (
    renouvellement_add, renouvellement_list, 
    renouvellement_update, renouvellement_view, 
    renouvellement_destroy, export_renouvellement_xls, export_renouvellement_csv, Export_Renouvellement_pdf)

app_name = 'renouvellement'

urlpatterns = [
    path('renouvellement_add/', renouvellement_add, name='renouvellement_add'),
    path('renouvellement_list/', renouvellement_list, name='renouvellement_list'),
    path('renouvellement_update/<int:id>/', renouvellement_update, name='renouvellement_update'),
    path('renouvellement_view/<int:id>/', renouvellement_view, name='renouvellement_view'),
    path('renouvellement_destroy/<int:id>/', renouvellement_destroy, name='renouvellement_destroy'),
    path('export/xls/', export_renouvellement_xls, name='export_renouvellement_xls'),
    path('export/csv/', export_renouvellement_csv, name='export_renouvellement_csv'),
    path('export/pdf/<int:id>/', Export_Renouvellement_pdf.as_view(), name='export_renouvellement_pdf'),
]
