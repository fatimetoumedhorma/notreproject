# Generated by Django 4.1.7 on 2023-07-01 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudiants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='note',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
    ]
