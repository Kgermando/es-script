from django import forms

from renouvellement.models import Renouvellement

from forms.statut import STATUTS
from contacts.models import Contact

class RenouvellementForm(forms.ModelForm):
    class Meta:
        model = Renouvellement
        fields = (
            'questions1', 'questions2', 'questions3', 'questions4', 'questions5', 'questions6', 'questions7', 'questions8', 'questions9',
            'questions10', 'questions12', 'questions13', 'questions15', 'questions16', 'Q19temps_a_contacter',
            'montant_de_pret', 'duree_de_credit', 'montant_a_rembourser_chaque_mois', 'montant_des_ventes_bonne_journee', 
            'montant_des_ventes_mauvaise_journee', 'date_a_laquelle_recevoir_credit', 'Nom_du_garant', 'Activite', 
            'Commentaire', 'Concurrent', 'CommentaireQ17', 'Statut', 'Contact', 'campaignname',
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

    questions1 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "questions1"
                }
            )
    )

    questions2 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "questions2"
                }
            )
    )

    questions3 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "questions3"
                }
            )
    )

    questions4 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "questions4"
                }
            )
    )

    questions5 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "questions5"
                }
            )
    )

    questions6 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "questions6"
                }
            )
    )

    questions7 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "questions7"
                }
            )
    )

    questions8 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "questions8"
                }
            )
    )

    questions9 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "questions9"
                }
            )
    )

    questions10 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "questions10"
                }
            )
    )

    questions12 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "questions12"
                }
            )
    )

    questions13 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "questions13"
            }
        )
    )

    questions15 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "questions15"
                }
            )
    )

    questions16 = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "questions16" 
                }
            )
    )

    Q19temps_a_contacter = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Q19temps_a_contacter"
                }
            )
    )

    montant_de_pret = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "montant_de_pret"
                }
            )
    )

    duree_de_credit = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "duree_de_credit"
                }
            )
    )

    montant_a_rembourser_chaque_mois = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "montant_a_rembourser_chaque_mois"
                }
            )
    )

    montant_des_ventes_bonne_journee = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "montant_des_ventes_bonne_journee"
                }
            )
    )

    montant_des_ventes_mauvaise_journee = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "montant_des_ventes_mauvaise_journee"
                }
            )
    )

    date_a_laquelle_recevoir_credit = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "date_a_laquelle_recevoir_credit"
                }
            )
    )

    Nom_du_garant = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nom_du_garant"
                }
            )
    )

    Activite = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Activite"
                }
            )
    )

    # Nom_societe = forms.CharField(
    #     label='',
    #     required=True,
    #     widget=forms.TextInput(
    #             attrs={
    #                 "class": "form-control",
    #                 "placeholder": "Nom_societe"
    #             }
    #         )
    # )
    
    
    Statut = forms.ChoiceField(
        label = '',
        required = True,
        choices = STATUTS,
        widget = forms.Select(
            attrs={
                "class": "form-control",
                "name":"Statut",
            }
        )
    )


    Commentaire = forms.CharField(
        label = '',
        required = True,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"Commentaire",
            }
        )
    )

    Concurrent = forms.CharField(
        label = '',
        required = True,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"Concurrent",
            }
        )
    )

    CommentaireQ17 = forms.CharField(
        label = '',
        required = True,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name":"CommentaireQ17",
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
