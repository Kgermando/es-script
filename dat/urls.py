
from django.urls import path

from dat.views import dat_add, dat_list, dat_update, dat_view, dat_destroy, export_dat_xls, export_dat_csv

app_name= 'dat'

urlpatterns = [
    path('dat-add/', dat_add, name='dat_add'),
    path('dat-list/', dat_list, name='dat_list'),
    path('dat-update/<int:id>/', dat_update, name='dat_update'),
    path('dat-view/<int:id>/', dat_view, name='dat_view'),
    path('dat-destroy/<int:id>/', dat_destroy, name='dat_destroy'),
    path('export/xls/', export_dat_xls, name='export_dat_xls'),
    path('export/csv/', export_dat_csv, name='export_dat_csv'),
]
