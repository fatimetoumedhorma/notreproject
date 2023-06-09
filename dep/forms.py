from django import forms
from .models import Departement

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ['id_departement', 'nom_departement']
        labels = {

      'id_departement': 'Code',
      'nom_departement': 'Nom_dep',
      
    }
    widgets = {
      'id_departement': forms.TextInput(attrs={'class': 'form-control'}),
      'nom_departement': forms.TextInput(attrs={'class': 'form-control'}),
      
    }
