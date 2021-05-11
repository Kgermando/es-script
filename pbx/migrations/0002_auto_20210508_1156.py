# Generated by Django 3.1.7 on 2021-05-08 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbx', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cdr',
            name='amaflags',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='ps_aors',
            name='max_contacts',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], verbose_name='max_contacts'),
        ),
        migrations.AlterField(
            model_name='sip_conf',
            name='amaflags',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default='billing', help_text='indicateurs spéciaux pour contrôler le calcul par défaut', max_length=20),
        ),
    ]