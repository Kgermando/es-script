# Generated by Django 3.1.7 on 2021-04-04 06:29

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(default='avatar.svg', upload_to='user-profile/')),
                ('birthday', models.IntegerField(null=True)),
                ('job', models.CharField(max_length=100, null=True)),
                ('bio', models.TextField(null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('contact_no', models.IntegerField(null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
