from django import forms
from encadrents.models import Encadrent
from dep.models import Departement
from .models import Groupe

class GroupeForm(forms.ModelForm):
    
    class Meta:
        model = Groupe
        fields = ['id_groupe', 'nom_groupe', 'id_departement', 'id']
        labels = {
            'id_groupe':'ID Groupe',
            'nom_groupe': 'Nom Groupe',
            'id_departement': 'ID departement',
            'id': 'ID Encadrent',
            
        }
        widgets = {
            'id_groupe': forms.TextInput(attrs={'class': 'form-control'}),
            'nom_groupe': forms.TextInput(attrs={'class': 'form-control'}),
            'id_departement': forms.Select(attrs={'class': 'form-control'}),
            'id': forms.Select(attrs={'class': 'form-control'}),
        }
        
#id_groupe = forms.ModelChoiceField(queryset=Groupe.objects.all())