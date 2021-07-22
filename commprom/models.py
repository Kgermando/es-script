from django.db import models
from django.contrib.auth.models import User

from contacts.models import Contact
from forms.statut import STATUTS

# Create your models here.
class Commprom(models.Model):
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date     = models.DateTimeField(auto_now_add=True)
    questions1       = models.CharField(max_length=200, null=True, default='-')
    questions2       = models.CharField(max_length=200, null=True, default='-')
    Contact          = models.ForeignKey(Contact, on_delete=models.CASCADE)
    Statut           = models.CharField(max_length=30, choices=STATUTS, null=True)
    Bound            = models.CharField(max_length=20, null=True)
    campaignname      = models.CharField(max_length=200, null=True, default='-')

    # def __str__(self):
    #     return self.Nom

