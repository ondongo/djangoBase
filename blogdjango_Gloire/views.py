from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home_view(request):
    # return HttpResponse('salut')
    return render(request,'home.html')

def contact_view(request):
    # return HttpResponse('Contactez moi')
    form=ContactForm()
    return render(request,'contact.html',{"form":form})

 