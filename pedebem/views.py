from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,loader
from .models import Pedidos
# Create your views here.

def index(request):
    template = loader.get_template("./templates/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def comandas(request):
    template = loader.get_template("./templates/comandas.html")
    cm = Pedidos.objects.all()
    context = {
        'cm': cm
    }
    return HttpResponse(template.render(context, request))
def teste(request):
    return HttpResponse("Teste.")