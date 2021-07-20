from rest_framework import serializers
from .models import *

class AcquisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acquisition
        fields = ['id', 'questions1', 'questions3', 'questions4', 'questions5',
                  'questions6', 'Contact', 'CommentaireQ5', 'CommentaireQ6', 'campaignname' ]
