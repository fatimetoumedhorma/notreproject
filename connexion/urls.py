from django.urls import path
from . import views
from django.contrib import admin







app_name = 'connexion'
urlpatterns=[
    path('inscription/',views.registerPage,name='inscription'),
    path('login/',views.loginPage,name='login'),
    path('acceul/',views.acceuil,name='acceuil'),

]