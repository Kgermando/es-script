from django.db import models
from django.contrib.auth.models import User


from forms.statut import STATUTS
from contacts.models import Contact
# Create your models here.
class Renouvellement(models.Model):
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date     = models.DateTimeField(auto_now_add=True)
    Contact          = models.ForeignKey(Contact, on_delete=models.CASCADE)
    questions1       = models.CharField(max_length=200, null=True, blank=True, default='-')
    questions2       = models.CharField(max_length=200, null=True, blank=True, default='-')
    questions3       = models.CharField(max_length=200, null=True, blank=True, default='-')
    questions4       = models.CharField(max_length=200, null=True, blank=True, default='-')
    questions5       = models.CharField(max_length=200, null=True, blank=True, default='-')
    questions6       = models.CharField(max_length=200, null=True, blank=True, default='-')
    questions7       = models.CharField(max_length=200, null=True, blank=True, default='-')
    questions8       = models.CharField(max_length=200, null=True, blank=True, default='-')
    questions9       = models.CharField(max_length=200, null=True, blank=True, default='-')
    questions10      = models.CharField(max_length=200, null=True, blank=True, default='-')
    # questions11      = models.CharField(max_length=200, null=True, blank=True)
    questions12      = models.CharField(max_length=200, null=True, blank=True, default='-')
    questions13      = models.CharField(max_length=200, null=True, blank=True, default='-')
    # questions14      = models.CharField(max_length=200, null=True, blank=True)
    questions15      = models.CharField(max_length=200, null=True, blank=True, default='-')
    questions16      = models.CharField(max_length=200, null=True, blank=True, default='-')
    # questions17      = models.CharField(max_length=200, null=True, blank=True)
    # questions18      = models.CharField(max_length=200, null=True, blank=True)
    Q19temps_a_contacter = models.CharField(max_length=200, null=True, blank=True, default='-')
    montant_de_pret                     = models.CharField(max_length=100, null=True, blank=True, default='-')
    duree_de_credit                     = models.CharField(max_length=100, null=True, blank=True, default='-')
    montant_a_rembourser_chaque_mois    = models.CharField(max_length=100, null=True, blank=True, default='-')
    montant_des_ventes_bonne_journee    = models.CharField(max_length=100, null=True, blank=True, default='-')
    montant_des_ventes_mauvaise_journee = models.CharField(max_length=100, null=True, blank=True, default='-')
    date_a_laquelle_recevoir_credit     = models.CharField(max_length=100, null=True, blank=True, default='-')
    Nom_du_garant   = models.CharField(max_length=100, null=True, blank=True, default='-')
    Activite        = models.CharField(max_length=100, null=True, blank=True, default='-')
    Statut          = models.CharField(max_length=30, choices=STATUTS, null=True, blank=True, default='-')
    Commentaire     = models.TextField(null=True, blank=True, default='-')
    Concurrent      = models.TextField(null=True, blank=True, default='-')
    CommentaireQ17  = models.TextField(null=True, blank=True, default='-')

