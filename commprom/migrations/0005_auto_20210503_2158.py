# Generated by Django 3.1.7 on 2021-05-03 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commprom', '0004_auto_20210503_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commprom',
            name='Remarque',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]