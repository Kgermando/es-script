# serializers.py
from rest_framework import serializers

from .models import Dat


class DatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dat
        fields = ['id', 'user', 'questions1', 'questions2', 'Contact', 'Statut', 'campaignname']
