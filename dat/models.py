from django.db import models
from django.contrib.auth.models import User

from forms.statut import STATUTS
from contacts.models import Contact
# Create your models here.
BOUND = (
    ('OUTBOUND', 'OUTBOUND'),
    ('INBOUND', 'INBOUND'),
)

class Dat(models.Model):
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date     = models.DateTimeField(auto_now_add=True)
    questions1       = models.CharField(max_length=200, null=True, default='-')
    questions2       = models.CharField(max_length=200, null=True, default='-')
    Contact          = models.ManyToManyField(Contact)
    Statut           = models.CharField(max_length=30, choices=STATUTS, null=True)
    Bound            = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.Nom

