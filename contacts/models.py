from django.db import models
from django.contrib.auth.models import User

from forms.pays import PAYS
from forms.province import PROVINCES
from forms.statut import STATUTS
# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    Nom             = models.CharField(max_length=100, null=True, blank=True, default='-')
    Post_Nom        = models.CharField(max_length=100, null=True, blank=True, default='-')
    Prenom          = models.CharField(max_length=100, null=True, blank=True, default='-')
    Numero          = models.CharField(max_length=20, null=True, blank=True, default='-', verbose_name='N°')
    Rue             = models.CharField(max_length=100, null=True, blank=True, default='-')
    Quartier        = models.CharField(max_length=100, null=True, blank=True, default='-')
    Commune         = models.CharField(max_length=100, null=True, blank=True, default='-')
    Ville           = models.CharField(max_length=100, null=True, blank=True, default='-')
    Province        = models.CharField(max_length=20, choices=PROVINCES, null=True, blank=True, default='-')
    # Pays            = models.CharField(max_length=100, choices=PAYS, null=True, blank=True, default='-')
    Tel1            = models.CharField(max_length=13, null=True, blank=True, default='-', verbose_name="Téléphone 1")
    Tel2            = models.CharField(max_length=13, null=True, blank=True, default='-', verbose_name="Téléphone 2")
    Tel3            = models.CharField(max_length=13, null=True, blank=True, default='-', verbose_name="Téléphone 3")
    Email           = models.EmailField(null=True, blank=True, default='contact@advans.com')
    Website         = models.URLField(null=True, blank=True, default='-', verbose_name="Site Web")
    Facebook        = models.CharField(max_length=100, null=True, blank=True, default='-')
    Instagram       = models.CharField(max_length=100, null=True, blank=True, default='-')
    Twitter         = models.CharField(max_length=100, null=True, blank=True, default='-')
    LinkedIn        = models.CharField(max_length=100, null=True, blank=True, default='-')
    Remarque        = models.CharField(max_length=200, null=True, blank=True, default='-')

    def __str__(self):
        return self.Nom 
