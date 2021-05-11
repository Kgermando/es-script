from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Campagne(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Profile(models.Model):

    ADMIN = 'Admin'
    SUPERVISOR = 'Supervisor'
    AGENT = 'Agent'
    CLIENT = 'Client'

    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('SUPERVISOR', 'Supervisor'),
        ('AGENT', 'Agent'),
        ('CLIENT', 'Client'),
    )

    SEXE = (
        ('FEMME', 'FEMME'),
        ('HOMME', 'HOMME'),
    )

    GENRE = (
        ('Madame', 'Madame'),
        ('Monsieur', 'Monsieur'),
    )

    profile_picture = models.ImageField(upload_to = 'user-profile/', default='images/user-bg.jpg')
    user            = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    campagne        = models.ForeignKey(Campagne, on_delete=models.CASCADE, max_length=100, null=True, blank=True)
    role            = models.CharField(choices=ROLE_CHOICES, max_length=100, null=True, blank=True)
    sexe            = models.CharField(choices=GENRE, max_length=100, null=True, blank=True)
    experience      = models.TextField(null=True, blank=True)
    adresse         = models.CharField(max_length=100, null=True, blank=True)
    contact_no      = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
