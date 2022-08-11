from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def utilisateurs_view(request):
    # return HttpResponse("user")
    return render(request,'utilisateurs/list.html')

def creer_view(request):
    return HttpResponse("creation_user")