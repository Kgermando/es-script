from rest_framework import serializers
from .models import *

class CommpromSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commprom
        fields = ['id', 'questions1', 'questions2',
                  'Statut', 'Bound', 'Contact', 'campaignname']
