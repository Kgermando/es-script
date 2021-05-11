
from django.urls import path

from contacts.views import contact_view, upload_csv
app_name= 'contacts'

urlpatterns = [
    path('contact_view/', contact_view, name='contact_view'),
    path('upload/csv/', upload_csv, name='upload_csv'),
]
