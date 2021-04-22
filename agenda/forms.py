from django.forms import ModelForm, DateInput
from agenda.models import Note, THEME
from django import forms

class NoteForm(ModelForm):
  class Meta:
    model = Note
    fields = ('title', 'description', 'theme',)

    title = forms.CharField(
      label='',
      required=True,
      widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Titre"
        }
      )
    )

    theme = forms.ChoiceField(
      label='',
      required=False,
      choices=THEME,
      widget=forms.Select(
        attrs={
            "id":"inputState",
            "class": "form-control",
            "placeholder": "Theme"
        }
      )
    )

    description = forms.CharField(
        label='Description',
        required=False,
        widget=forms.Textarea(
          attrs={
            "class": "form-control",
            "placeholder": "Description...",
            "rows":"3"
          }
        )
    )

