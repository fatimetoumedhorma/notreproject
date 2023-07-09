from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from .models import Departement
from .forms import DepartementForm
from etudiants.models import Etudiant
from django.contrib.auth.models import User
# from connexion.models import CustomUser




def accueil(request):
    # etudient = Etudiant.objects.get(user=request.user)
    return render(request, 'accueil.html')


def dep(request):
    mymembers = Departement.objects.all().values()
    template = loader.get_template('dep.html')
    context = {'mymembers': mymembers, }
    return HttpResponse(template.render(context, request))

def view_dep(request, id_departement):
    mymembers = Departement.objects.get(pk=id_departement)
    template = loader.get_template('dep.html')
    context = {'mymembers': mymembers, }
    return HttpResponse(template.render(context, request))

def adddep(request):
    
    if request.method == 'POST':
        
        form = DepartementForm(request.POST)
        if form.is_valid():
            
            nouveau_code = form.cleaned_data['id_departement']
            nouveau_nom = form.cleaned_data['nom_departement']

            nouveau_departement = Departement(
                id_departement=nouveau_code,
                nom_departement=nouveau_nom
            )
            nouveau_departement.save()

            form = DepartementForm()
            context = {'form': form, 'success': True}
            return render(request, 'adddep.html', context)
        
    else:
        
        form = DepartementForm()


    context = {'form': form}
    return render(request, 'adddep.html', context)


def updatedep(request, id_departement):
    mymembers = get_object_or_404(Departement, pk=id_departement)

    if request.method == 'POST':
        form = DepartementForm(request.POST, instance=mymembers)
        if form.is_valid():
            form.save()
            template = loader.get_template('updatedep.html')
            context = {'mymembers': mymembers, 'form': form, 'success': True}
            return HttpResponse(template.render(context, request))
    else:
        form = DepartementForm(instance=mymembers)
    
    context = {'form': form}
    return render(request, 'updatedep.html', context)


def deletedep(request, id_departement):
  if request.method == 'POST':
    member = Departement.objects.get(pk=id_departement)
    member.delete()
  return HttpResponseRedirect(reverse('dep'))
        
          
                                
    
 


        
       
    
  
    

 






