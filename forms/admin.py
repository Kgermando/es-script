from django.contrib import admin

from forms.models import Kyc
# Register your models here.
@admin.register(Kyc)
class scriptAdmin(admin.ModelAdmin):
    list_display = (
        'Nom_societe','Nom','Post_Nom','Prenom','Numero','Quartier','Commune','Province',
            'Pays','Tel1','Tel2','Email','Website','Facebook','Instagram', 'Twitter','LinkedIn',
    )