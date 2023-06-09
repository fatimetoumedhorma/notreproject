from django.db import models
from groupes.models import Groupe
from dep.models import Departement

class Etudiant(models.Model):
    id_etudiant = models.AutoField(primary_key=True)
    nom_etudiant = models.CharField(max_length=100)
    prenom_etudiant = models.CharField(max_length=100)
    id_groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    id_departement = models.ForeignKey(Departement, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom_etudiant} {self.prenom_etudiant}"




# Create your models here.
