from django.db import models
from groupes.models import Groupe

class Sujet(models.Model):
    id_sujet = models.AutoField(primary_key=True)
    titre_sujet = models.CharField(max_length=255)
    id_groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre_sujet



# Create your models here.
