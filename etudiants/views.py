from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from .models import Etudiant
from groupes.models import Groupe
from dep.models import Departement
from django.shortcuts import render, redirect
from .forms import EtudiantForm



def etud(request):
    mymembers = Etudiant.objects.all().values()
    template = loader.get_template('etud.html')
    context = {'mymembers': mymembers, }
    return HttpResponse(template.render(context, request))

def view_etud(request, id_etudiant):
    etudiant = get_object_or_404(Etudiant, pk=id_etudiant)
    context = {'etudiant': etudiant}
    return render(request, 'view_etud.html', context)

def addetud(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etud')  # Rediriger vers la liste des sujets après l'ajout
    else:
        form = EtudiantForm()
    context = {'form': form}
    return render(request, 'addetud.html', context)


def updateetud(request, id_etudiant):
    etudiant = get_object_or_404(Etudiant, id_etudiant=id_etudiant)

    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            context = {'etudiant': etudiant, 'form': form, 'success': True}
            return render(request, 'updateetud.html', context)
    else:
        form = EtudiantForm(instance=etudiant)
    
    context = {'etudiant': etudiant, 'form': form}
    return render(request, 'updateetud.html', context)

def deleteetud(request, id_etudiant):
  if request.method == 'POST':
    member = Etudiant.objects.get(pk=id_etudiant)
    member.delete()
  return HttpResponseRedirect(reverse('etud'))


    

# Create your views here.
