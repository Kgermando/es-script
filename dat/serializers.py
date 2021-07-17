# serializers.py
from rest_framework import serializers

from .models import Dat


class DatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dat
        fields = ('user', 'questions1', 'questions2', 'Contact', 'Statut')

