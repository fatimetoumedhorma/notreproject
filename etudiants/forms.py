from django import forms
from groupes.models import Groupe
from dep.models import Departement
from .models import Etudiant

class EtudiantForm(forms.ModelForm):
    #id_groupe = forms.ModelChoiceField(queryset=Groupe.objects.all())
    class Meta:
        model = Etudiant
        fields = ['id_etudiant', 'nom_etudiant', 'prenom_etudiant', 'id_groupe', 'id_departement']
        labels = {
            'id_etudiant': 'ID Etudiantt',
            'nom_etudiant': 'Nom Etudiant',
            'prenom_etudiant': 'Prenom Etudiant',
            'id_groupe': 'ID Groupe',
            'id_departement': 'Departement',
        }
        widgets = {
            'id_etudiant': forms.TextInput(attrs={'class': 'form-control'}),
            'nom_etudiant': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom_etudiant': forms.TextInput(attrs={'class': 'form-control'}),
            'id_groupe': forms.Select(attrs={'class': 'form-control'}),
            'id_departement': forms.Select(attrs={'class': 'form-control'}),
        }
