from django.shortcuts import render
# from .db_articles import articles
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect

from django.urls import reverse
from .models import Article
from .forms import ArticleForm
#Gérer les erreurs 404 différement
from django.shortcuts import get_object_or_404
# Create your views here.
def articles_view(request):
    #Récupérer tous les articles avec le objects.all
    
    #Requete article récent
    articles=Article.objects.all().order_by('-date_publication')
    
    
    return render(request,'articles/list.html',context={'all_articles':articles})

# def article_view(request,slug):
#     try:
#     #1er parametre le champ(field) 2e parametre la valeur
#         article=Article.objects.get(slug=slug)
#         return render(request,'articles/detail.html',context={"article":article})
#     except Article.DoesNotExist:
#         raise Http404('Article pas trouvé')   

def article_view(request,slug):

   
    article=get_object_or_404(Article,slug=slug)
        
   
    return render(request,'articles/detail.html',context={"article":article})
  
    # return HttpResponse("page de slug")
    # for article in articles:
    #     if article['slug']==slug:
    #         # return HttpResponse(article["contenu"])
    #         return render(request,'articles/detail.html',context={'article':article})
    # return HttpResponse("Wow toi là pas d'article en vue")
 
 
def creer_view(request):  
    #Afficher le formulaire
    form=ArticleForm()
    if request.method=='POST':
        #enregistre dans la base de données si requete POST
        form=ArticleForm(request.POST)
        form.save()
        # return HttpResponseRedirect('/Articles/')
        return HttpResponseRedirect(reverse('articles:articles'))
        
    return render(request,'articles/creer.html',context={'form':form})