
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    
    #Creation news Urls
    
    path('',views.utilisateurs_view,name='utilisateurs'),
    #Chemin qui vienne après L'url de base 
     path('creer/',views.creer_view,name='creer'),
    
]
