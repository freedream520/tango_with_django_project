from django.conf.urls import patterns, url 
from rango import views 

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),     
        url(r'^add_category', views.add_category, name='add_category'),
        #子串匹配到的内容将可以用命名的name参数来提取
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', 
            views.category, name='category'),
        )
        
        