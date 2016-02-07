from django.shortcuts import render
from django.http import HttpResponse

def index(request):#request is HttpRequest object 
    return HttpResponse('Rango says hey there world!<br/><a href="/rango/about">about</a>')
    
def about(request):
    return HttpResponse('Here is the about page.<br/> <a href="/rango/">main page</a>')
