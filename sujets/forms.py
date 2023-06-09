from django import forms
from groupes.models import Groupe
from .models import Sujet

class SujetForm(forms.ModelForm):
    #id_groupe = forms.ModelChoiceField(queryset=Groupe.objects.all())
    class Meta:
        model = Sujet
        fields = ['id_sujet', 'titre_sujet', 'id_groupe']
        labels = {
            'id_sujet': 'ID Sujet',
            'titre_sujet': 'Titre du sujet',
            'id_groupe': 'ID Groupe',
        }
        widgets = {
            'id_sujet': forms.TextInput(attrs={'class': 'form-control'}),
            'titre_sujet': forms.TextInput(attrs={'class': 'form-control'}),
            'id_groupe': forms.Select(attrs={'class': 'form-control'}),
        }
