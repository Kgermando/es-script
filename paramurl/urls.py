
from django.urls import path

from paramurl.views import paramurl_view

app_name= 'param_url'

urlpatterns = [
    path('text/', paramurl_view),
]
