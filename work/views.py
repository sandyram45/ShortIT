from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Article

def home(request):
    article_obj = Article.objects.get(id=3)
    article_title = article_obj.title
    article_content = article_obj.content
    return HttpResponse("Hello World!")