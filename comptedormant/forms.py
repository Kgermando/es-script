from django import forms

from comptedormant.models import Compte_dormant
 
from contacts.models import Contact
from forms.statut import STATUTS

class Compte_dormantForm(forms.ModelForm):
    class Meta:
        model = Compte_dormant
        fields = (
            'questions1', 'questions2', 'questions3', 'questions4', 
            'Raison', 'Statut', 'Bound', 'Contact', 'campaignname',
        ) 

    questions1 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"questions1"
            }
        )
    ) 

    questions2 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"questions2"
            }
        )
    )

    questions3 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"questions3"
            }
        )
    )

    questions4 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"questions4"
            }
        )
    )

    Raison = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"Raison"
            }
        )
    )

    Contact = forms.ModelChoiceField(
        label='',
        required=False,
        queryset= Contact.objects.all().order_by('-created_date'),
        widget=forms.Select(
            attrs={
                "id": "inputState",
                "class": "form-control",
                "placeholder": "Hopital"
            }
        )
    )

    Statut = forms.ChoiceField(
        label = '',
        required=True,
        choices = STATUTS,
        widget = forms.Select(
            attrs={
                "class": "form-control",
                "name":"Statut",
            }
        )
    )

    Bound = forms.CharField(
        label = '',
        required=False,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "Bound",
            }
        )
    )

    Remarque = forms.CharField(
        label = '',
        required=False,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "Remarque",
            }
        )
    )

    campaignname = forms.CharField(
        label = '',
        required = True,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"campaignname",
            }
        )
    )

