from django.contrib import admin
from django.urls import path
from .import views

#Namespacing
app_name="articles"
urlpatterns = [
   
    path('',views.articles_view,name='articles'),
    path('creer/',views.creer_view,name="creer"),
    path('<slug:slug>/',views.article_view,name='article'),
    ]
   
