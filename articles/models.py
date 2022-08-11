from django.db import models

# Create your models here.

#partie base de données
class Article(models.Model):
    titre=models.CharField(max_length=150)
    contenu=models.TextField()
    slug=models.SlugField(max_length=100)
    date_publication=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titre