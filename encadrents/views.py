from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Encadrent

from .forms import EncadrentForm



def index(request):

    return render(request,'encadrents/index.html', {
        'encadrentss': Encadrent.objects.all()

        
    })


def view_encadrent(request, id):
    encadrent = Encadrent.objects.get(pk=id)
    return render(request, 'encadrents/index.html', {'encadrents': [encadrent]})


def add(request):
  if request.method == 'POST':
    form = EncadrentForm(request.POST)
    if form.is_valid():
      
      nouveau_nom= form.cleaned_data['nom']
      nouveau_prenom = form.cleaned_data['prenom']
      nouveau_email = form.cleaned_data['email']
      

      nouveau_encadrent = Encadrent(
        
        nom=nouveau_nom,
        prenom=nouveau_prenom,
        email=nouveau_email,

      )
      nouveau_encadrent.save()
      return render(request, 'encadrents/add.html', {
        'form': EncadrentForm(),
        'success': True
      })
  else:
    form = EncadrentForm()
  return render(request, 'encadrents/add.html', {
    'form': EncadrentForm()
  })

def edit(request, id):
  if request.method == 'POST':
    encadrent = Encadrent.objects.get(pk=id)
    form = EncadrentForm(request.POST, instance=encadrent)
    if form.is_valid():
      form.save()
      return render(request, 'encadrents/edit.html', {
        'form': form,
        'success': True
      })
  else:
    encadrent = Encadrent.objects.get(pk=id)
    form = EncadrentForm(instance=encadrent)
  return render(request, 'encadrents/edit.html', {
    'form': form
  })
def delete(request, id):
  if request.method == 'POST':
    encadrent = Encadrent.objects.get(pk=id)
    encadrent.delete()
  return HttpResponseRedirect(reverse('index'))











# Create your views here.
