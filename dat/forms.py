from django import forms

from dat.models import Dat
from contacts.models import Contact

from forms.statut import STATUTS

class DatForm(forms.ModelForm):
    class Meta:
        model = Dat
        fields = (
            'questions1', 'questions2', 'Contact', 'Statut', 'Bound',
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

    Contact = forms.ModelChoiceField(
        label='',
        required=False,
        queryset= Contact.objects.all().order_by('-created_date'),
        widget=forms.Select(
            attrs={
                "id": "inputState",
                "class": "form-control",
                "placeholder": "Contact"
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


