from django.db import models
from django.contrib.auth.models import User

from forms.pays import PAYS
from forms.province import PROVINCES
from forms.statut import STATUTS
# Create your models here.
class Kyc(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
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
    Nom_societe     = models.CharField(max_length=200, null=True, blank=True, default='-', verbose_name="Nom de la société")
    Nom             = models.CharField(max_length=100, null=True, blank=True, default='-')
    Post_Nom        = models.CharField(max_length=100, null=True, blank=True, default='-')
    Prenom          = models.CharField(max_length=100, null=True, blank=True, default='-')
    Numero          = models.CharField(max_length=20, null=True, blank=True, default='-', verbose_name='N°')
    Quartier        = models.CharField(max_length=100, null=True, blank=True, default='-')
    Commune         = models.CharField(max_length=100, null=True, blank=True, default='-')
    Province        = models.CharField(max_length=20, choices=PROVINCES, null=True, blank=True, default='-')
    Pays            = models.CharField(max_length=100, choices=PAYS, null=True, blank=True, default='-')
    Tel1            = models.CharField(max_length=13, null=True, blank=True, default='-', verbose_name="Téléphone 1")
    Tel2            = models.CharField(max_length=13, null=True, blank=True, default='-', verbose_name="Téléphone 2")
    Email           = models.EmailField(null=True, blank=True, default='-')
    Website         = models.URLField(null=True, blank=True, default='-', verbose_name="Site Web")
    Facebook        = models.CharField(max_length=100, null=True, blank=True, default='-')
    Instagram       = models.CharField(max_length=100, null=True, blank=True, default='-')
    Twitter         = models.CharField(max_length=100, null=True, blank=True, default='-')
    LinkedIn        = models.CharField(max_length=100, null=True, blank=True, default='-')
    Statut          = models.CharField(max_length=30, choices=STATUTS, null=True, blank=True, default='-')
    Remarque        = models.TextField(null=True, blank=True, default='-')
    Commentaire     = models.TextField(null=True, blank=True, default='-')
    Concurrent      = models.TextField(null=True, blank=True, default='-')
    CommentaireQ17  = models.TextField(null=True, blank=True, default='-')

    # def __str__(self):
    #     return self.Nom_societe + ' ' + self.Nom + ' ' + self.Post_Nom + ' ' + self.Prenom

# class Contact(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_date = models.DateTimeField(auto_now_add=True)
#     Nom             = models.CharField(max_length=100, null=True, blank=True, default='-')
#     Post_Nom        = models.CharField(max_length=100, null=True, blank=True, default='-')
#     Prenom          = models.CharField(max_length=100, null=True, blank=True, default='-')
#     Numero          = models.CharField(max_length=20, null=True, blank=True, default='-', verbose_name='N°')
#     Rue             = models.CharField(max_length=100, null=True, blank=True, default='-')
#     Quartier        = models.CharField(max_length=100, null=True, blank=True, default='-')
#     Commune         = models.CharField(max_length=100, null=True, blank=True, default='-')
#     Ville           = models.CharField(max_length=100, null=True, blank=True, default='-')
#     Province        = models.CharField(max_length=20, choices=PROVINCES, null=True, blank=True, default='-')
#     # Pays            = models.CharField(max_length=100, choices=PAYS, null=True, blank=True, default='-')
#     Tel1            = models.CharField(max_length=13, null=True, blank=True, default='-', verbose_name="Téléphone 1")
#     Tel2            = models.CharField(max_length=13, null=True, blank=True, default='-', verbose_name="Téléphone 2")
#     Email           = models.EmailField(null=True, blank=True, default='-')
#     Website         = models.URLField(null=True, blank=True, default='-', verbose_name="Site Web")
#     Facebook        = models.CharField(max_length=100, null=True, blank=True, default='-')
#     Instagram       = models.CharField(max_length=100, null=True, blank=True, default='-')
#     Twitter         = models.CharField(max_length=100, null=True, blank=True, default='-')
#     LinkedIn        = models.CharField(max_length=100, null=True, blank=True, default='-')
#     Remarque        = models.CharField(max_length=200, null=True, blank=True, default='-')
    
#     def __str__(self):
#         return self.Nom


