
from django.urls import path

from acquisition.views import (
    acquisition_add, acquisition_list,
     acquisition_update, acquisition_view, 
     acquisition_destroy, export_acquisition_xls, export_acquisition_csv)

app_name = 'acquisition'

urlpatterns = [
    path('acquisition_add/', acquisition_add, name='acquisition_add'),
    path('acquisition_list/', acquisition_list, name='acquisition_list'),
    path('acquisition_update/<int:id>/', acquisition_update, name='acquisition_update'),
    path('acquisition_view/<int:id>/', acquisition_view, name='acquisition_view'),
    path('acquisition_destroy/<int:id>/', acquisition_destroy, name='acquisition_destroy'),
    path('export/xls/', export_acquisition_xls, name='export_acquisition_xls'),
    path('export/csv/', export_acquisition_csv, name='export_acquisition_csv'),
]
 