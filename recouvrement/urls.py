
from django.urls import path

from recouvrement.views import (
    recouvrement_add, recouvrement_list, 
    recouvrement_view, recouvrement_update, 
    recouvrement_destroy, export_recouvrement_xls, export_recouvrement_csv)

app_name= 'recouvrement'

urlpatterns = [
    path('recouvrement_add/', recouvrement_add, name='recouvrement_add'),
    path('recouvrement_list/', recouvrement_list, name='recouvrement_list'),
    path('recouvrement_view/<int:id>/', recouvrement_view, name='recouvrement_view'),
    path('recouvrement_update/<int:id>/', recouvrement_update, name='recouvrement_update'),
    path('recouvrement_destroy/<int:id>/', recouvrement_destroy, name='recouvrement_destroy'),
    path('export/xls/', export_recouvrement_xls, name='export_recouvrement_xls'),
    path('export/csv/', export_recouvrement_csv, name='export_recouvrement_csv'),
]
