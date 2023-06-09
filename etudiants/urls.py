from django.urls import path
from . import views


urlpatterns = [
    #path('', views.index, name='index'),
    
    path('', views.etud, name='etud'),
    path('etudiants/<int:id_etudiant>/', views.view_etud, name='view_etud'),
    path('addetud/', views.addetud, name='addetud'),
    path('updateetud/<int:id_etudiant>/', views.updateetud, name='updateetud'),
    path('deleteetud/<int:id_etudiant>/', views.deleteetud, name='deleteetud'),
    
    




]