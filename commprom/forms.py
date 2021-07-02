from django import forms

from commprom.models import Commprom

from contacts.models import Contact
from forms.statut import STATUTS

class CommpromForm(forms.ModelForm):
    class Meta:
        model = Commprom
        fields = (
            'questions1', 'questions2', 'Statut', 'Bound', 'Contact',
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


