from django import forms

from recouvrement.models import Recouvrement

from contacts.models import Contact
from forms.statut import STATUTS

class RecouvrementForm(forms.ModelForm):
    class Meta:
        model = Recouvrement
        fields = (
            'questions1', 'questions2', 'Statut', 'Bound', 'Contact', 'campaignname',
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

    Contact = forms.ModelChoiceField(
        label='',
        required=False,
        queryset=Contact.objects.all().order_by('-created_date'),
        widget=forms.Select(
            attrs={
                "id": "inputState",
                "class": "form-control",
                "placeholder": "Hopital"
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

