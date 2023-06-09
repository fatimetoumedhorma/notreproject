from django import forms
from .models import Encadrent


class EncadrentForm(forms.ModelForm):

  class Meta:
    model = Encadrent
    fields = ['nom', 'prenom', 'email']
    labels = {

      'nom': 'Nom',
      'prenom': 'Prenom',
      'email': 'Email',
    }
    widgets = {
      'nom': forms.TextInput(attrs={'class': 'form-control'}),
      'prenom': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
    }
  