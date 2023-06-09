from django.urls import path
from . import views


urlpatterns = [
    #path('', views.index, name='index'),
    
    path('', views.grp, name='grp'),
    path('groupes/<int:id_groupe>/', views.view_grp, name='view_grp'),
    path('addgrp/', views.addgrp, name='addgrp'),
    path('updategrp/<int:id_groupe>/', views.updategrp, name='updategrp'),
    path('deletegrp/<int:id_groupe>/', views.deletegrp, name='deletegrp'),



]
