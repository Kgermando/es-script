# Generated by Django 3.1.7 on 2021-07-19 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comptedormant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compte_dormant',
            name='campaignname',
            field=models.CharField(default='-', max_length=200, null=True),
        ),
    ]
