from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page 
from rango.forms import CategoryForm, PageForm

def index(request):#request is HttpRequest object 
    #从 model 中取出 top 5，传递到 templates 中 
    category_list = Category.objects.order_by('-likes')[:5] # '-' 降序
    context_dict = {'categories': category_list}
    
    page_list = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = page_list
    
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
        
def add_category(request):
    """
    功能：
    显示表格
    保存提交的数据到数据库
    或者显示错误
    """
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            #Call the index() view 
            #显示主页
            return index(request)
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    
    return render(request, 'rango/add_category.html', {'form': form})
    
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        category = None 
        
    if request.method == 'POST':
        form = PageForm(request.POST)
        
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0 
                page.save()
                return category(reqeust, category_name_slug)
            else:
                print(form.errors)
        else:
            form = PageForm()
            
        context_dict = {'form': form, 'category': category}
        
    return render(request, 'rango/add_page.html', context_dict)
    
        
        
