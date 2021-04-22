from django.urls import path

from pbx.views import cdr_view, cdr_detail, cel_view, cel_detail

app_name = 'pbx'

urlpatterns = [
    path('pbx/cdr/', cdr_view, name='cdr_view'),
    path('pbx/cdr/<int:uniqueid>/', cdr_detail, name='cdr_detail'),
    path('pbx/cel/', cel_view, name='cel_view'),
    path('pbx/cel/<int:uniqueid>/', cel_detail, name='cel_detail'),
]
