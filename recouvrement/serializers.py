from rest_framework import serializers
from .models import *

class RecouvrementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recouvrement
        fields = ['id', 'questions1', 'questions2',
                  'Statut', 'Bound', 'Contact', 'campaignname']
