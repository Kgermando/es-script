from rest_framework import serializers
from .models import *


class RenouvellementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renouvellement
        fields = ['id', 'questions1', 'questions2', 'questions3', 'questions4', 'questions5', 'questions6', 'questions7', 'questions8', 'questions9',
            'questions10', 'questions12', 'questions13', 'questions15', 'questions16', 'Q19temps_a_contacter',
            'montant_de_pret', 'duree_de_credit', 'montant_a_rembourser_chaque_mois', 'montant_des_ventes_bonne_journee', 
            'montant_des_ventes_mauvaise_journee', 'date_a_laquelle_recevoir_credit', 'Nom_du_garant', 'Activite', 
            'Commentaire', 'Concurrent', 'CommentaireQ17', 'Statut', 'Contact','campaignname']
