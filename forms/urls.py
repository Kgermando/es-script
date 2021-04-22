
from django.urls import path

from forms.views import forms_view, enquetes_view

app_name= 'forms'

urlpatterns = [
    path('', forms_view, name='forms_view'),
    path('enquetes_view/', enquetes_view, name='enquetes_view'),
]
