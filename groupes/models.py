from django.db import models
from dep.models import Departement
from encadrents.models import Encadrent

class Groupe(models.Model):
    id_groupe = models.AutoField(primary_key=True)
    nom_groupe = models.CharField(max_length=100)
    id_departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    id  = models.ForeignKey(Encadrent, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_groupe



# Create your models here.
