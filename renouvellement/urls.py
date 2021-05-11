
from django.urls import path

from renouvellement.views import renouvellement_add, renouvellement_list, renouvellement_update, renouvellement_view, renouvellement_destroy

app_name = 'renouvellement'

urlpatterns = [
    path('renouvellement_add/', renouvellement_add, name='renouvellement_add'),
    path('renouvellement_list/', renouvellement_list, name='renouvellement_list'),
    path('renouvellement_update/<int:id>/', renouvellement_update, name='renouvellement_update'),
    path('renouvellement_view/<int:id>/', renouvellement_view, name='renouvellement_view'),
    path('renouvellement_destroy/<int:id>/', renouvellement_destroy, name='renouvellement_destroy')
]
