import os 
#默认设置文件定位 settings.py 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page 

def populate():
    python_category = add_category('Python', views=128, likes=64)
    
    add_page(category=python_category,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/")
        
    add_page(category=python_category,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/")
        
    add_page(category=python_category,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/")
        
    django_category = add_category('Django', views=64, likes=32)
    
    add_page(category=django_category,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")
        
    add_page(category=django_category,
        title="Django Rocks",
        url="http://www.djangorocks.com/")
        
    add_page(category=django_category,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/")
        
    frame_category = add_category("Other Frameworks", views=32, likes=16)
    
    add_page(category=frame_category,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/")
        
    add_page(category=frame_category,
        title="Flask",
        url="http://flask.pocoo.org")
        
    #打印出添加的东西
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p.title)))
    
def add_page(category, title, url, views=0):
    p = Page.objects.get_or_create(category=category, title=title, 
                                    url=url, views=views)[0] #tuple 中的第一个    
    return p 
    
def add_category(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    return c 
    
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()