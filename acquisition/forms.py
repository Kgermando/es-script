from django import forms

from acquisition.models import Acquisition, SERVICES
from contacts.models import Contact
from forms.statut import STATUTS

# Forms 
class AcquisitionForm(forms.ModelForm):
    class Meta:
        model = Acquisition
        fields = (
            'questions1', 'questions3', 'questions4', 'questions5', 'questions6', 'Contact', 'CommentaireQ5', 'CommentaireQ6', 'campaignname',
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
