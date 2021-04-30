# Generated by Django 3.1.7 on 2021-04-24 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210423_2115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='address',
            new_name='adresse',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='experiance',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='job',
        ),
        migrations.AddField(
            model_name='profile',
            name='sexe',
            field=models.CharField(blank=True, choices=[('FEMME', 'FEMME'), ('HOMME', 'HOMME')], max_length=100, null=True),
        ),
    ]
