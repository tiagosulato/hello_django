from django.shortcuts import HttpResponse

def hello(request,nome,idade):
    return HttpResponse('<h1>Hello, {} de {} anos </h1>'.format(nome, idade))
