
from django.urls import path

from dashboard.views import dashboard_view, dashboard_admin_view

app_name= 'dashboard'

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('dashboard_admin_view/', dashboard_admin_view, name='dashboard_admin_view'),
]
