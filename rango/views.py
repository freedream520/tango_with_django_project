from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rango.models import Category, Page 
from rango.forms import CategoryForm, PageForm, \
    UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required

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
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None 
        
    if request.method == 'POST':
        form = PageForm(request.POST)        
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0 
                page.save()
                return category(request, category_name_slug)
        else:
            print(form.errors)
    else:
        form = PageForm()
            
    context_dict = {'form':form, 'category': cat}
        
    return render(request, 'rango/add_page.html', context_dict)
    
def register(request):
    #告诉 template 是否注册成功，初始为 False 
    registered = False 
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            #通过 save() 将表单中的数据储存到变量中
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            #还需要放入东西，所以 commit=False ，
            #为什么 user 中不要？ wait
            profile = profile_form.save(commit=False)
            profile.user = user 
            
            #如果提供了图片，就将图片放入 UserProfile 模块
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                
            profile.save()            
            registered = True 
            
            return HttpResponseRedirect('/rango/login/')
            
        #表格无效或其他错误
        else:
            print(user_form.errors, profile_form.errors)
    #不是 POST 请求，我们渲染表格给用户输入
    else:
        #UserForm 是 Model，加上括号是其的一个 object 
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    return render(request, 'rango/register.html', 
        {'user_form': user_form, 'profile_form': profile_form, 
            'registered': registered})
        
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        #验证 username and password 是否有效
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                #重定向
                return HttpResponseRedirect('/rango/')
            else:
                return HttpResponse('Your Rango account is disabled.')
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'rango/login.html', {})
        
@login_required 
def restricted(request):
    return HttpResponse("You are logged in.")
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rango/')
    
        
