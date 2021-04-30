from django.contrib import admin

from agenda.models import Note
# Register your models here.
class AgendaAdmin(admin.ModelAdmin):
    pass

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'theme', 'created_date', 'user',
    )
