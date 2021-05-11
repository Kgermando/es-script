from django import forms

from commprom.models import Commprom

from forms.province import PROVINCES
from forms.statut import STATUTS

class CommpromForm(forms.ModelForm):
    class Meta:
        model = Commprom
        fields = (
            'questions1', 'questions2', 'Nom','Post_Nom',
            'Prenom','Numero', 'Rue', 'Quartier', 'Commune', 'Ville', 'Province',
            'Tel1','Email', 'Statut', 'Bound', 'Remarque',
        )

    questions1 = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "questons1"
            }
        )
    )

    questions2 = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "questons2"
            }
        )
    )

    Nom = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nom",
                "name": "Nom",
            }
        )
    )

    Post_Nom = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "Post_Nom",
            }
        )
    )

    Prenom = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "Prenom",
            }
        )
    )

    Numero = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "Numero",
            }
        )
    )

    Rue = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "Rue",
            }
        )
    )

    Quartier = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "Quartier",
            }
        )
    )

    Commune = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "Commune",
            }
        )
    )

    Ville = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "Ville",
            }
        )
    )

    Province = forms.ChoiceField(
        label='',
        required=False,
        choices=PROVINCES,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "name": "Province",
            }
        )
    )

    Tel1 = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "Tel1",
            }
        )
    )

    Email = forms.EmailField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "Email",
            }
        )
    )

    Statut = forms.ChoiceField(
        label='',
        required=True,
        choices=STATUTS,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "name": "Statut",
            }
        )
    )

    Remarque = forms.CharField(
        label = '',
        required = False,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "Remarque",
            }
        )
    )

