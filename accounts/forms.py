from django import forms

from django.contrib.auth.models import User

class SignInForm(forms.ModelForm):
    class Meta:
        field = ('username', 'password')
        model = User

    username = forms.CharField(
        label = 'Username',
        required = True,
        widget = forms.TextInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Non d'utilisateur"   
            }
        )
    )

    password = forms.CharField(
        label = 'Mot de passe'
        required = True
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Mot de passe" 
            }
        )
    )


