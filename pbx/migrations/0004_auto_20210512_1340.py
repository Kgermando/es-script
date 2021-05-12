# Generated by Django 3.1.7 on 2021-05-12 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbx', '0003_auto_20210508_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoints',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='ps_aors',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='ps_auths',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='sip_conf',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='sippeers',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='voicemail',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Unique ID'),
        ),
    ]
