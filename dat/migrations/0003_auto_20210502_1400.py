# Generated by Django 3.1.7 on 2021-05-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dat', '0002_auto_20210502_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dat',
            name='Bound',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dat',
            name='Province',
            field=models.CharField(blank=True, choices=[('Bas-Uele', 'Bas-Uele'), ('Équateur', 'Équateur'), ('Haut-Katanga', 'Haut-Katanga'), ('Haut-Lomami', 'Haut-Lomami'), ('Haut-Uele', 'Haut-Uele'), ('Ituri', 'Ituri'), ('Kasaï', 'Kasaï'), ('Kasaï-Central', 'Kasaï-Central'), ('Kasaï oriental', 'Kasaï oriental'), ('Kinshasa', 'Kinshasa'), ('Kongo central1', 'Kongo central1'), ('Kwango', 'Kwango'), ('Kwilu', 'Kwilu'), ('Lomami', 'Lomami'), ('Lualaba', 'Lualaba'), ('Mai-Ndombe', 'Mai-Ndombe'), ('Maniema', 'Maniema'), ('Mongala', 'Mongala'), ('Nord-Kivu', 'Nord-Kivu'), ('Nord-Ubangi', 'Nord-Ubangi'), ('Sankuru', 'Sankuru'), ('Sud-Kivu', 'Sud-Kivu'), ('Sud-Ubangi', 'Sud-Ubangi'), ('Tanganyika', 'Tanganyika'), ('Tshopo', 'Tshopo'), ('Tshuapa', 'Tshuapa')], default='Kinshasa', max_length=20, null=True),
        ),
    ]
