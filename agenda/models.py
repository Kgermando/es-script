from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

THEME = (
    ('bg-primary', 'Blue'),
    ('bg-success', 'Vert'), 
    ('bg-warning', 'Jaune'),
    ('bg-dark', 'Noir'),
    ('bg-pink', 'Violet'),
    ('bg-danger', 'Rouge'), 
)

# Create your models here.
class Note(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    theme = models.CharField(max_length=15, choices=THEME)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('agenda:note_detail', args=(self.id,))
