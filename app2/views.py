from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hell(request):
    return HttpResponse('<h1 style="color:red";><i>this is hell my world</i>')
def heaven(request):
    return HttpResponse('<i>heaven is a lie</i>')