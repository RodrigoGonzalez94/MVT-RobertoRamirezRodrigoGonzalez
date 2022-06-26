from re import template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from entregable.models import Familiares

# Create your views here.

def una_vista(request):
    return HttpResponse('<h1>Datos de Familiares</h1>')

def un_template(request):
    
    # template = loader.get_template('index.html')
    
    familiares1 = Familiares(nombre = 'Luisa', edad = 43, fecha_nacimiento = '1978-08-25')
    familiares2 = Familiares(nombre = 'Ivan', edad = 29, fecha_nacimiento = '1992-09-17')
    familiares3 = Familiares(nombre = 'Luis', edad = 17, fecha_nacimiento = '2005-01-11')
    familiares1.save()
    familiares2.save()
    familiares3.save()
    
    # render = template.render({'lista_objetos': [familiares1, familiares2, familiares3]})
    # return HttpResponse(render)
    
    return render(request, 'index.html', {'lista_objetos': [familiares1, familiares2, familiares3]})
    # return render(request, 'index.html', {'lista_objetos': [familiares]})

def listado_de_familiares(request):
    
    template = loader.get_template('listado_de_familiares.html')
    
    lista_familiares = Familiares.objects.all()
    
    render = template.render({'lista_familiares': lista_familiares})
    
    return HttpResponse(render)