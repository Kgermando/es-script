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
            'questions1', 'questions2', 'questions3', 'questions4', 'questions5', 'questions6', 'questions7', 'questions8', 'questions9',
            'questions10', 'questions12', 'questions13', 'questions15', 'questions16', 'Q19temps_a_contacter',
            'montant_de_pret', 'duree_de_credit', 'montant_a_rembourser_chaque_mois', 'montant_des_ventes_bonne_journee', 
            'montant_des_ventes_mauvaise_journee', 'date_a_laquelle_recevoir_credit', 'Nom_du_garant', 'Activite', 
            'Remarque', 'Commentaire', 'Concurrent', 'CommentaireQ17',
            'Nom_societe','Nom','Post_Nom','Prenom','Numero','Quartier','Commune','Province',
            'Pays','Tel1','Tel2','Email','Website','Facebook','Instagram', 'Twitter','LinkedIn', 'Statut',
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
                    "name": "Province",
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
                    "name":"Statut",
                }
            )
        )

        Remarque = forms.CharField(
            label = '',
            required = True,
            widget = forms.TextInput(
                attrs={
                    "class": "form-control",
                    "name":"Remarque",
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

