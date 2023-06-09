from django.db import models

class Departement(models.Model):
    id_departement = models.CharField(max_length=50, primary_key=True)
    nom_departement = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_departement


# Create your models here.
