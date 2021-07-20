from django.db import models
from django.contrib.auth.models import User

from contacts.models import Contact

from forms.statut import STATUTS
# Create your models here.

SERVICES = (
    ('Crédit', 'Crédit'),
    ('Comptes/épargne', 'Comptes/épargne'),
    ('Les deux', 'Les deux'),
    ('Autres', 'Autres'),
)

class Acquisition(models.Model):
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date     = models.DateTimeField(auto_now_add=True)
    questions1       = models.CharField(max_length=200, null=True, default='-')
    # questions2       = models.CharField(max_length=200, null=True, default='-')
    questions3       = models.CharField(max_length=200, choices=SERVICES, null=True, default='-')
    questions4       = models.CharField(max_length=200, null=True, default='-')
    questions5       = models.CharField(max_length=200, null=True, default='-')
    questions6       = models.CharField(max_length=200, null=True, default='-')
    Contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    Statut           = models.CharField(max_length=30, choices=STATUTS, null=True)
    CommentaireQ5    = models.CharField(max_length=200, null=True, blank=True, default='-')
    CommentaireQ6    = models.CharField(max_length=200, null=True, blank=True, default='-')
    campaignname      = models.CharField(max_length=200, null=True, default='-')

    def __str__(self):
        return self.questions1
 