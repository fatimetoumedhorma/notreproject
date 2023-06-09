from django.urls import path
from . import views


urlpatterns = [
    #path('', views.index, name='index'),
    
    path('', views.suj, name='suj'),
    path('sujets/<int:id_sujet>/', views.view_suj, name='view_suj'),
    path('addsuj/', views.addsuj, name='addsuj'),
    path('updatesuj/<int:id_sujet>/', views.updatesuj, name='updatesuj'),
    path('deletesuj/<int:id_sujet>/', views.deletesuj, name='deletesuj'),
    
    




]