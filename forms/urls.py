
from django.urls import path

from forms.views import (scripting_forms, enquetes_view, scripting_list, scripting_forms_edit)

app_name= 'forms'

urlpatterns = [
    path('', scripting_forms, name='scripting_forms'),
    path('scripting_list/', scripting_list, name='scripting_list'),
    path('scripting_forms_edit/<int:id>/', scripting_forms_edit, name='scripting_forms_edit'),
    path('enquetes_view/', enquetes_view, name='enquetes_view'),
]
