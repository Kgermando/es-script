
from django.urls import path

from paramurl.views import paramurl_view

app_name= 'paramurl'

urlpatterns = [
    path('text/?<phonenuber>&<campaign>', paramurl_view, name='paramurl_view'),
]
