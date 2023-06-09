from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('encadrents/<int:id>/', views.view_encadrent, name='view_encadrent'),
    path('add/', views.add, name='add'),
    path('encadrents/edit/<int:id>/', views.edit, name='edit'),
    path('encadrents/delete/<int:id>/', views.delete, name='delete'),
]