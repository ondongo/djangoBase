
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #Creation news Urls
    
    path('',views.home_view,name='home'),
    path('contact/',views.contact_view,name='contact'),
    path('Articles/',include('articles.urls')),
    path('utilisateurs/',include('utilisateurs.urls')),
]
