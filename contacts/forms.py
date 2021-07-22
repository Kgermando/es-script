from django import forms

from contacts.models import Contact
from forms.province import PROVINCES 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'Nom', 'Post_Nom', 'Prenom', 'Numero', 'Rue', 'Quartier', 'Commune', 'Ville', 'Province', 'phonenumber', 'Tel2', 'Tel3',
            'Email', 'Website', 'Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'Remarque'
        )

        Nom = forms.CharField(
            label='',
            required=False,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "Nom",
                    "placeholder": "Nom"
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

        Province = forms.CharField(
            label='',
            required=False,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "name": "Province",
                }
            )
        )

        # Province = forms.ChoiceField(
        #     label='',
        #     required=False,
        #     choices=PROVINCES,
        #     widget=forms.Select(
        #         attrs={
        #             "class": "form-control",
        #             "id": "Province",
        #             "name": "Province",
        #         }
        #     )
        # )

        phonenumber = forms.CharField(
            label='',
            required=False,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "name": "phonenumber",
                }
            )
        )

        Tel2 = forms.CharField(
            label='',
            required=False,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "name": "Tel2",
                }
            )
        )

        Tel3 = forms.CharField(
            label='',
            required=False,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "name": "Tel3",
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

        Website = forms.URLField(
            label='',
            required=False,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "name": "Website",
                }
            )
        )

        Facebook = forms.CharField(
            label='',
            required=False,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "name": "Facebook",
                }
            )
        )

        Instagram = forms.CharField(
            label='',
            required=False,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "name": "Instagram",
                }
            )
        )

        Twitter = forms.CharField(
            label='',
            required=False,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "name": "Twitter",
                }
            )
        )

        LinkedIn = forms.CharField(
            label='',
            required=False,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "name": "LinkedIn",
                    "placeholder": "LinkedIn"
                }
            )
        )

        Remarque = forms.CharField(
            label='',
            required=False,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "name": "Remarque",
                    "placeholder": "Remarque"
                }
            )
        )
        
