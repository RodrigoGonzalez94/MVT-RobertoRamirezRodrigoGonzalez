from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def una_vista(request):
    return HttpResponse('<h1>Datos de Familiares</h1>')

def un_template(request):
    return HttpResponse('<h1>Datos de Familiares otra vista</h1>')