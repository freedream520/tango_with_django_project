from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page 

def index(request):#request is HttpRequest object 
    #从 model 中取出 top 5，传递到 templates 中 
    category_list = Category.objects.order_by('-likes')[:5] # '-' 降序
    context_dict = {'categories': category_list}
    
    return render(request, 'rango/index.html', context_dict)
    
def category(request, category_name_slug):
    context_dict = {}
    
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category'] = category
        context_dict['category_name'] = category.name        
        
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages 
    except Category.DoesNotExist:
        #不做任何事， templates 显示 'no category'
        pass 
    
    return render(request, 'rango/category.html', context_dict)
        
        
        
