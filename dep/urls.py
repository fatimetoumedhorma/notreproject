from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    #path('', views.index, name='index'),
    
    path('', views.dep, name='dep'),
    path('admin/',admin.site.urls),
    path('dep/<str:id_departement>/', views.view_dep, name='view_dep'),
    path('adddep/', views.adddep, name='adddep'),
    path('updatedep/<str:id_departement>/', views.updatedep, name='updatedep'),
    path('deletedep/<str:id_departement>/', views.deletedep, name='deletedep'),




]




