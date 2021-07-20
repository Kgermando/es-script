from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework import filters
from rest_framework import generics, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from acquisition.models import Acquisition
from acquisition.serializers import AcquisitionSerializer

from commprom.models import Commprom
from commprom.serializers import CommpromSerializer

from comptedormant.models import Compte_dormant
from comptedormant.serializers import Compte_dormantSerializer

from dat.models import Dat
from dat.serializers import DatSerializer

from recouvrement.models import Recouvrement
from recouvrement.serializers import RecouvrementSerializer

from renouvellement.models import Renouvellement
from renouvellement.serializers import RenouvellementSerializer


class GlobalSearchAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': Acquisition.objects.all(), 'serializer_class': AcquisitionSerializer},
        {'queryset': Commprom.objects.all(), 'serializer_class': CommpromSerializer},
        {'queryset': Compte_dormant.objects.all(), 'serializer_class': Compte_dormantSerializer},
        {'queryset': Dat.objects.all(), 'serializer_class': DatSerializer},
        {'queryset': Recouvrement.objects.all(),'serializer_class': RecouvrementSerializer},
        {'queryset': Renouvellement.objects.all(), 'serializer_class': RenouvellementSerializer},
    ]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['phonenumber', 'campaignname']
    filter_backends = [filters.SearchFilter]
    search_fields = ['contact', 'campaignname', ]
