from django.urls import path

from issabel.views import cdr_issabel, cel_issabel, cdr_issabel_detail, cel_issabel_detail

app_name = 'issabel'

urlpatterns = [
    path('issabel/cdr/', cdr_issabel, name='cdr_issabel'),
    path('issabel/cdr/<int:uniqueid>/', cdr_issabel_detail, name='cdr_issabel_detail'),
    path('issabel/cel/', cel_issabel, name='cel_issabel'),
    path('issabel/cel/<int:uniqueid>/', cel_issabel_detail, name='cel_issabel_detail'),
]
