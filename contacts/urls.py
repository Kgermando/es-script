
from django.urls import path

from contacts.views import contact_view, upload_contact_csv, export_contact_csv, export_contact_xls, export_contact_pdf
app_name= 'contacts'

urlpatterns = [
    path('contact_view/', contact_view, name='contact_view'),
    path('upload/csv/', upload_contact_csv, name='upload_contact_csv'),
    path('export/xls/', export_contact_xls, name='export_contact_xls'), 
    path('export/csv/', export_contact_csv, name='export_contact_csv'),
    path('export/pdf/', export_contact_pdf, name='export_contact_pdf'),
]
