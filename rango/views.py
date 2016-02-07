from django.shortcuts import render
from django.http import HttpResponse

def index(request):#request is HttpRequest object 
    context_dict = {'boldmessage': "I am bold font from the context."}
    
    return render(request, 'rango/index.html', context_dict)
    
def about(request):
    return HttpResponse('Here is the about page.<br/> <a href="/rango/">main page</a>')
