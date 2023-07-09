from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from etudiants.models import Etudiant
# Create your views here.


def acceuil(request):
    return render(request,'acceuil.html')


def registerPage(request):
    form = CreateUserForm()
    if request.method=="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'compt creer aavrc success pour'+ user)
            
    context={'form': form}
    return render(request,'inscription.html',context)

def loginPage(request):
    if request.method =="POST":
     username=request.POST.get('username')
     password=request.POST.get('password')
     user=authenticate(request,username=username,password=password)
     if user is not None:
        login(request,user)
        if user.role=='admin':

         return redirect('admin:index')
        else:
           return redirect('partie_utilisat')
    #  else:
    #     return render(request)
    context={}
    return render(request,'login.html',context)

def acceuil(request):
    user=request.user
    etud=Etudiant.objects.get(request.user)
    return render(request,'acceuil.html')
# Create your views here.
