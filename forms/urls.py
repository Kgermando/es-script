
from django.urls import path

from forms.views import (scripting_forms, enquetes_view, scripting_list, scripting_forms_edit, contact_view, upload_csv)

app_name= 'forms'

urlpatterns = [
    path('', scripting_forms, name='scripting_forms'),
    path('scripting_list/', scripting_list, name='scripting_list'),
    path('scripting_forms_edit/<int:id>/', scripting_forms_edit, name='scripting_forms_edit'),
    path('contact_view/', contact_view, name='contact_view'),
    path('upload/csv/', upload_csv, name='upload_csv'),
    path('enquetes_view/', enquetes_view, name='enquetes_view'),
]
