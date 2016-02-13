from django.conf import settings #相当于 project 中的 settings.py 
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #匹配到  ^rango 就使用 rango.urls 中的匹配
    url(r'^rango/', include('rango.urls')),
    url(r'accounts/', include('registration.backends.simple.urls')),
)

#对所有 以 media/ 开头的请求将会传递给 'django.views.static'——视图函数 static
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve', #名字？
        {'document_root': settings.MEDIA_ROOT}),)#MEDIA_ROOT 设置为存放文件的目录

INSTALLED_APPS = (
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'rango',
)