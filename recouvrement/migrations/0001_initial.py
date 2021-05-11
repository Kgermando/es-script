# Generated by Django 3.1.7 on 2021-05-04 04:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recouvrement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('questions1', models.CharField(default='-', max_length=200, null=True)),
                ('questions2', models.CharField(default='-', max_length=200, null=True)),
                ('Nom', models.CharField(blank=True, default='-', max_length=100, null=True)),
                ('Post_Nom', models.CharField(blank=True, default='-', max_length=100, null=True)),
                ('Prenom', models.CharField(blank=True, default='-', max_length=100, null=True)),
                ('Numero', models.CharField(blank=True, default='-', max_length=20, null=True, verbose_name='N°')),
                ('Quartier', models.CharField(blank=True, default='-', max_length=100, null=True)),
                ('Commune', models.CharField(blank=True, default='-', max_length=100, null=True)),
                ('Province', models.CharField(blank=True, choices=[('--------', '--------'), ('Bas-Uele', 'Bas-Uele'), ('Équateur', 'Équateur'), ('Haut-Katanga', 'Haut-Katanga'), ('Haut-Lomami', 'Haut-Lomami'), ('Haut-Uele', 'Haut-Uele'), ('Ituri', 'Ituri'), ('Kasaï', 'Kasaï'), ('Kasaï-Central', 'Kasaï-Central'), ('Kasaï oriental', 'Kasaï oriental'), ('Kinshasa', 'Kinshasa'), ('Kongo central1', 'Kongo central1'), ('Kwango', 'Kwango'), ('Kwilu', 'Kwilu'), ('Lomami', 'Lomami'), ('Lualaba', 'Lualaba'), ('Mai-Ndombe', 'Mai-Ndombe'), ('Maniema', 'Maniema'), ('Mongala', 'Mongala'), ('Nord-Kivu', 'Nord-Kivu'), ('Nord-Ubangi', 'Nord-Ubangi'), ('Sankuru', 'Sankuru'), ('Sud-Kivu', 'Sud-Kivu'), ('Sud-Ubangi', 'Sud-Ubangi'), ('Tanganyika', 'Tanganyika'), ('Tshopo', 'Tshopo'), ('Tshuapa', 'Tshuapa')], default='Kinshasa', max_length=20, null=True)),
                ('Tel1', models.CharField(blank=True, default='-', max_length=13, null=True)),
                ('Email', models.EmailField(blank=True, default='contact@advans.com', max_length=254, null=True)),
                ('Statut', models.CharField(choices=[('Statuts de reporting', 'Statuts de reporting'), ('Accord', 'Accord'), ('Déjà payé son crédit', 'Déjà payé son crédit'), ('Refus', 'Refus'), ('Rappel', 'Rappel (interlocuteur demande de rappeler)'), ('Injoignable', 'Injoignable'), ('Absent', 'Absent'), ('Faux numéro', 'Faux numéro'), ('Réfléchir', 'Réfléchir')], max_length=30, null=True)),
                ('Bound', models.CharField(max_length=20, null=True)),
                ('Remarque', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
