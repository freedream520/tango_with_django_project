from django.conf.urls import patterns, url 
from rango import views 

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),        
        #子串匹配到的内容将可以用命名的name参数来提取
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', 
            views.category, name='category'),
        )
        #\w a-z, A-Z, 0-9, including the _
        #\- 指 '-' 匹配 a-z, A-Z, 0-9 _ and - 
        #<category_name_slug> 与 views.py 中的参数名一样
        