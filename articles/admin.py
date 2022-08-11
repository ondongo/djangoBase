from django.contrib import admin

# Register your models here.
from .models import Article

#Sur l'interface USER de django
admin.site.register(Article)
