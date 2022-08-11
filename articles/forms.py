from django.forms import ModelForm

from .models import Article
#Class du formulaire
class ArticleForm(ModelForm):
    class Meta:
        model=Article
        fields= ['titre','contenu','slug']