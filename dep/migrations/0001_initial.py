# Generated by Django 4.2.1 on 2023-05-27 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id_departement', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nom_departement', models.CharField(max_length=100)),
            ],
        ),
    ]