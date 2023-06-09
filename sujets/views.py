from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from .models import Sujet
from groupes.models import Groupe
from django.shortcuts import render, redirect
from .forms import SujetForm



def suj(request):
    mymembers = Sujet.objects.all().values()
    template = loader.get_template('suj.html')
    context = {'mymembers': mymembers, }
    return HttpResponse(template.render(context, request))

def view_suj(request, id_sujet):
    sujet = get_object_or_404(Sujet, pk=id_sujet)
    context = {'sujet': sujet}
    return render(request, 'view_suj.html', context)

def addsuj(request):
    if request.method == 'POST':
        form = SujetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suj')  # Rediriger vers la liste des sujets après l'ajout
    else:
        form = SujetForm()
    context = {'form': form}
    return render(request, 'addsuj.html', context)


def updatesuj(request, id_sujet):
    sujet = get_object_or_404(Sujet, id_sujet=id_sujet)

    if request.method == 'POST':
        form = SujetForm(request.POST, instance=sujet)
        if form.is_valid():
            form.save()
            context = {'sujet': sujet, 'form': form, 'success': True}
            return render(request, 'updatesuj.html', context)
    else:
        form = SujetForm(instance=sujet)
    
    context = {'sujet': sujet, 'form': form}
    return render(request, 'updatesuj.html', context)

def deletesuj(request, id_sujet):
  if request.method == 'POST':
    member = Sujet.objects.get(pk=id_sujet)
    member.delete()
  return HttpResponseRedirect(reverse('suj'))


    