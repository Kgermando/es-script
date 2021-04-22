from django import forms

from forms.models import Kyc
from forms.pays import PAYS
from forms.province import PROVINCES
from forms.statut import STATUTS
# Create your forms here.
class KycForm(forms.ModelForm):
    class Meta:
        model = Kyc
        fields = (
            'questons1',
            'Nom_societe','Nom','Post_Nom','Prenom','Numero','Quartier','Commune','Province',
            'Pays','Tel1','Tel2','Email','Website','Facebook','Instagram', 'Twitter','LinkedIn', 'Statut',
        )

        question1 = forms.BooleanField(
            label = '',
            required = True,
            widget=forms.CheckboxInput(
                    attrs={
                    "id":"question1",
                    "value": "false",
                    "class": "form-check-input",
                    "placeholder": "Questions"
                }
            )
        )

        Nom_societe = forms.CharField(
            label='',
            required=True,
            widget=forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "Nom_societe"
                    }
                )
        )
        
        Nom = forms.CharField(
            label='',
            required=True,
            widget=forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "Nom"
                    }
                )
        )

        Post_Nom = forms.CharField(
            label = '',
            required = True,
            widget = forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "Post_Nom",
                    "name":"Post_Nom",
                }
            )
        )

        Prenom = forms.CharField(
            label = '',
            required = True,
            widget = forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "Prenom",
                    "name":"Prenom",
                }
            )
        )

        Numero = forms.CharField(
            label = '',
            required = True,
            widget = forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "Numero",
                    "name":"Numero",
                }
            )
        )

        Quartier = forms.CharField(
            label = '',
            required = True,
            widget = forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "Quartier",
                    "name":"Quartier",
                }
            )
        )

        Commune = forms.CharField(
            label = '',
            required = True,
            widget = forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "Commune",
                    "name":"Commune",
                }
            )
        )

        Province = forms.ChoiceField(
            label = '',
            required = True,
            choices = PROVINCES,
            widget = forms.Select(
                attrs={
                    "class": "form-control",
                    "id": "Province",
                    "name": "select",
                }
            )
        )

        Pays = forms.ChoiceField(
            label = '',
            required = True,
            choices = PAYS,
            widget = forms.Select(
                attrs={
                    "class": "form-control",
                    "id": "Pays",
                    "name":"Pays",
                }
            )
        )

        Tel1 = forms.CharField(
            label = '',
            required = True,
            widget = forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "Tel1",
                    "name":"Tel1",
                }
            )
        )

        Tel2 = forms.CharField(
            label = '',
            required = True,
            widget = forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "Tel2",
                    "name":"Tel2",
                }
            )
        )

        Email = forms.EmailField(
            label = '',
            required = True,
            widget = forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "Email",
                    "name":"Email",
                }
            )
        )

        Website = forms.URLField(
            label = '',
            required = True,
            widget = forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "Website",
                    "name":"Website",
                }
            )
        )

        Facebook = forms.CharField(
            label = '',
            required = True,
            widget = forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "Facebook",
                    "name":"Facebook",
                }
            )
        )

        Instagram = forms.CharField(
            label = '',
            required = True,
            widget = forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "Instagram",
                    "name":"Instagram",
                }
            )
        )

        Twitter = forms.CharField(
            label = '',
            required = True,
            widget = forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "Twitter",
                    "name":"Twitter",
                }
            )
        )

        LinkedIn = forms.CharField(
            label = '',
            required = True,
            widget = forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "LinkedIn",
                    "name":"LinkedIn",
                }
            )
        )
        
        Statut = forms.ChoiceField(
            label = '',
            required = True,
            choices = STATUTS,
            widget = forms.Select(
                attrs={
                    "class": "form-control",
                    "id": "Statut",
                    "name":"Statut",
                }
            )
        )
