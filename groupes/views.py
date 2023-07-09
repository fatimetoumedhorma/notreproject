from django.shortcuts import render
from encadrents.models import Encadrent
from dep.models import Departement
from .models import Groupe
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from .forms import GroupeForm



def grp(request):

    mymembers = Groupe.objects.select_related('id').all()

    template = loader.get_template('grp.html')
    context = {'mymembers': mymembers, }
    return HttpResponse(template.render(context, request))

def view_grp(request, id_groupe):
    groupe = get_object_or_404(Groupe, pk=id_groupe)
    context = {'groupe': groupe}
    return render(request, 'view_suj.html', context)

def addgrp(request):
    if request.method == 'POST':
        form = GroupeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grp')  # Rediriger vers la liste des sujets après l'ajout
    else:
        form = GroupeForm()
    context = {'form': form}
    return render(request, 'addgrp.html', context)

def updategrp(request, id_groupe):
    groupe = get_object_or_404(Groupe, id_groupe=id_groupe)

    if request.method == 'POST':
        form = GroupeForm(request.POST, instance=groupe)
        if form.is_valid():
            form.save()
            context = {'groupe': groupe, 'form': form, 'success': True}
            return render(request, 'updategrp.html', context)
    else:
        form = GroupeForm(instance=groupe)
    
    context = {'groupe': groupe, 'form': form}
    return render(request, 'updategrp.html', context)

def deletegrp(request, id_groupe):
  if request.method == 'POST':
    member = Groupe.objects.get(pk=id_groupe)
    member.delete()
  return HttpResponseRedirect(reverse('grp'))





# Create your views here.
