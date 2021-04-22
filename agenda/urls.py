from django.urls import path

from agenda.views import agenda_view, agenda_detail, note_view, note_detail, NoteDeleteView

app_name = 'agenda'

urlpatterns = [
    path('agenda_view/', agenda_view, name='agenda_view'),
    path('agenda_detail/', agenda_detail, name='agenda_detail'),
    path('notes/note_view/', note_view, name='note_view'),
    path('notes/note_detail/<int:id>/', note_detail, name='note_detail'),
    path('notes/<int:pk>/remove', NoteDeleteView.as_view(), name="remove_note"),
]
