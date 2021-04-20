
from django.urls import path

from forms.views import forms_view

app_name= 'forms'

urlpatterns = [
    path('', forms_view, name='forms_view'),
]
