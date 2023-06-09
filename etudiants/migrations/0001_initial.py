# Generated by Django 4.2.1 on 2023-05-27 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groupes', '0001_initial'),
        ('dep', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id_etudiant', models.AutoField(primary_key=True, serialize=False)),
                ('nom_etudiant', models.CharField(max_length=100)),
                ('prenom_etudiant', models.CharField(max_length=100)),
                ('id_departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dep.departement')),
                ('id_groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groupes.groupe')),
            ],
        ),
    ]
