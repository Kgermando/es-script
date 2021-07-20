from rest_framework import serializers
from .models import *

class Compte_dormantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compte_dormant
        fields = ['id', 'questions1', 'questions2', 'questions3', 'questions4', 
                  'Raison', 'Statut', 'Bound', 'Contact', 'campaignname']
