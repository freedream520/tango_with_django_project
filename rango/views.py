from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):#request is HttpRequest object 
    #从 model 中取出 top 5，传递到 templates 中 
    category_list = Category.objects.order_by('-likes')[:5] # '-' 降序
    context_dict = {'categories': category_list}
    
    return render(request, 'rango/index.html', context_dict)
    
def about(request):
    return render(request, 'rango/about.html')
