from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response
# request handler or in others its called an action

def addition():
    x = 1
    y = 2
    return x + y


def say_hello(request):
    test = addition()

    return render(request, 'hello.html', {'name': 'Mosh'})

def default(request):
    return render(request, 'index.html')