from django.shortcuts import render
from django.http import HttpResponse

def index(request):#request is HttpRequest object 
    return HttpResponse('Rango says hey there world!')
