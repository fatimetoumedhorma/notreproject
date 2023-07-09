# Generated by Django 4.1.7 on 2023-07-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connexion', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('utilisateur', 'Utilisateur')], default='utilisateur', max_length=20),
        ),
    ]
