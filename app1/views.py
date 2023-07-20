from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('<i>good morning</i>')
def hii(request):
    return HttpResponse('<i>welcome to dubai</i>')