from django import forms

from acquisition.models import Acquisition, SERVICES
from forms.province import PROVINCES
from forms.statut import STATUTS

# Forms 
class AcquisitionForm(forms.ModelForm):
    class Meta:
        model = Acquisition
        fields = (
            'questions1', 'questions3', 'questions4', 'questions5', 'questions6', 
            'Nom', 'Post_Nom', 'Prenom', 'Numero', 'Rue', 'Quartier', 'Commune', 'Ville', 'Province', 
            'Tel1', 'Email', 'Statut', 'Bound', 'Remarque', 'CommentaireQ5', 'CommentaireQ6',
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

    # questions2 = forms.CharField(
    #     label='',
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "name":"questions2"
    #         }
    #     )
    # )

    questions3 = forms.ChoiceField(
        label = '',
        required=False,
        choices = SERVICES,
        widget = forms.Select(
            attrs={
                "class": "form-control",
                "name": "questions3",
            }
        )
    )

    questions4 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"question4"
            }
        )
    )

    questions5 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"question5"
            }
        )
    )

    questions6 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"question6"
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
                "name":"Nom",
            }
        )
    )

    Post_Nom = forms.CharField(
        label = '',
        required=False,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"Post_Nom",
            }
        )
    )

    Prenom = forms.CharField(
        label = '',
        required=False,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"Prenom",
            }
        )
    )

    Numero = forms.CharField(
        label = '',
        required=False,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"Numero",
            }
        )
    )

    Rue = forms.CharField(
        label = '',
        required=False,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"Rue",
            }
        )
    )

    Quartier = forms.CharField(
        label = '',
        required=False,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"Quartier",
            }
        )
    )

    Commune = forms.CharField(
        label = '',
        required=False,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"Commune",
            }
        )
    )

    Ville = forms.CharField(
        label = '',
        required=False,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"Ville",
            }
        )
    )

    Province = forms.ChoiceField(
        label = '',
        required=False,
        choices = PROVINCES,
        widget = forms.Select(
            attrs={
                "class": "form-control",
                "name": "Province",
            }
        )
    )

    Tel1 = forms.CharField(
        label = '',
        required=False,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"Tel1",
            }
        )
    )

    Email = forms.EmailField(
        label = '',
        required=False,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"Email",
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

    CommentaireQ5 = forms.CharField(
        label = '',
        required=False,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "CommentaireQ5",
            }
        )
    )

    CommentaireQ6 = forms.CharField(
        label = '',
        required=False,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "CommentaireQ6",
            }
        )
    )