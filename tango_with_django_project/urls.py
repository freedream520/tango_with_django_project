from django.conf import settings #相当于 project 中的 settings.py 
from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

#注册成功后转向 index 页面
class MyRegistrationView(RegistrationView):
    #The URL to redirect to after successful registration
    def get_success_url(self, request, user):        
        return '/rango/'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #匹配到  ^rango 就使用 rango.urls 中的匹配
    url(r'^rango/', include('rango.urls')),
                                #as_view() 给 Class 提供一个函数入口
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),    
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