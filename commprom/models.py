from django.db import models
from django.contrib.auth.models import User

from forms.province import PROVINCES
from forms.statut import STATUTS

# Create your models here.
class Commprom(models.Model):
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date     = models.DateTimeField(auto_now_add=True)
    questions1       = models.CharField(max_length=200, null=True, default='-')
    questions2       = models.CharField(max_length=200, null=True, default='-')
    Nom              = models.CharField(max_length=100, null=True, blank=True, default='-')
    Post_Nom         = models.CharField(max_length=100, null=True, blank=True, default='-')
    Prenom           = models.CharField(max_length=100, null=True, blank=True, default='-')
    Numero           = models.CharField(max_length=20, null=True, blank=True, default='-', verbose_name='N°')
    Rue              = models.CharField(max_length=100, null=True, blank=True, default='-')
    Quartier         = models.CharField(max_length=100, null=True, blank=True, default='-')
    Commune          = models.CharField(max_length=100, null=True, blank=True, default='-')
    Ville            = models.CharField(max_length=100, null=True, blank=True, default='-')
    Province         = models.CharField(max_length=20, choices=PROVINCES, null=True, blank=True, default='Kinshasa')
    Tel1             = models.CharField(max_length=13, null=True, blank=True, default='-')
    Email            = models.EmailField(null=True, blank=True, default='contact@advans.com')
    Statut           = models.CharField(max_length=30, choices=STATUTS, null=True)
    Bound            = models.CharField(max_length=20, null=True)
    Remarque         = models.CharField(max_length=200, null=True, blank=True, default='-')

    def __str__(self):
        return self.Nom

