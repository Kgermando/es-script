from django.db import models
from django.contrib.auth.models import User

from forms.pays import PAYS
from forms.province import PROVINCES
from forms.statut import STATUTS
# Create your models here.
class Kyc(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    questons1       = models.BooleanField(null=True)
    questons2       = models.BooleanField(null=True)
    questons3       = models.BooleanField(null=True)
    questons4       = models.BooleanField(null=True)
    questons5       = models.BooleanField(null=True)
    questons6       = models.BooleanField(null=True)
    questons7       = models.BooleanField(null=True)
    questons8       = models.BooleanField(null=True)
    questons9       = models.BooleanField(null=True)
    questons10      = models.BooleanField(null=True)
    questons11      = models.BooleanField(null=True)
    questons12      = models.BooleanField(null=True)
    questons13      = models.BooleanField(null=True)
    questons10      = models.BooleanField(null=True)
    questons11      = models.BooleanField(null=True)
    questons12      = models.BooleanField(null=True)
    questons13      = models.BooleanField(null=True)
    questons14      = models.BooleanField(null=True)
    questons15      = models.BooleanField(null=True)
    questons16      = models.BooleanField(null=True)
    questons17      = models.BooleanField(null=True)
    questons18      = models.BooleanField(null=True)
    questons19      = models.BooleanField(null=True)
    Nom_societe     = models.CharField(max_length=200, null=True, blank=True, verbose_name="Nom de la société")
    Nom             = models.CharField(max_length=100, null=True, blank=True)
    Post_Nom        = models.CharField(max_length=100, null=True, blank=True)
    Prenom          = models.CharField(max_length=100, null=True, blank=True)
    Numero          = models.CharField(max_length=20, null=True, blank=True, verbose_name='N°')
    Quartier        = models.CharField(max_length=100, null=True, blank=True)
    Commune         = models.CharField(max_length=100, null=True, blank=True)
    Province        = models.CharField(max_length=20, choices=PROVINCES, null=True, blank=True)
    Pays            = models.CharField(max_length=100, choices=PAYS, null=True, blank=True)
    Tel1            = models.CharField(max_length=13, null=True, blank=True, verbose_name="Téléphone 1")
    Tel2            = models.CharField(max_length=13, null=True, blank=True, verbose_name="Téléphone 2")
    Email           = models.EmailField(null=True, blank=True)
    Website         = models.URLField(null=True, blank=True, verbose_name="Site Web")
    Facebook        = models.CharField(max_length=100, null=True, blank=True)
    Instagram       = models.CharField(max_length=100, null=True, blank=True)
    Twitter         = models.CharField(max_length=100, null=True, blank=True)
    LinkedIn        = models.CharField(max_length=100, null=True, blank=True)
    Statut          = models.CharField(max_length=30, choices=STATUTS, null=True, blank=True)
    Remarque        = models.TextField()
    
    def __str__(self):
        return self.Nom_societe + ' ' + self.Nom + ' ' + self.Post_Nom + ' ' + self.Prenom
    
