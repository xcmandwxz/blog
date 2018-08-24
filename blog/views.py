from django.shortcuts import render
from .models import *



def index(request):

    article = Article.objects.all()
    id = article.order_by('-id')[0:]


    title1 = article.get(id=1).Atitle
    # title2 = article.get(id=2).Atitle
    jianjie1 = article.get(id=1).Ajian
    # jianjie2 = article.get(id=2).Ajian
    context = {
        'title1':title1,
        # 'title2':title2,
        'jianjie1':jianjie1,
        # 'jianjie2':jianjie2
        'ids':id
    }




    return render(request,'index.html',context)


def login(request):
    return render(request,'login.html')


