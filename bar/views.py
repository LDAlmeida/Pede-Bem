from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from bar.models import Comanda, ComandaItens, Item
from .serializers import ComandaSerializer, ItemSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class Comandas(viewsets.ModelViewSet):
    queryset = Comanda.objects.exclude(status='Paga')
    serializer_class = ComandaSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def comanda_detail(request, pk):
    """
    Retrieve, update or delete a code Comanda.
    """
    print(pk)
    try:
        comanda = Comanda.objects.get(pk=pk)
    except comanda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ComandaSerializer(comanda)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ComandaSerializer(comanda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comanda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Itens(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def itens_detail(request, pk):
    """
    Retrieve, update or delete a code Comanda.
    """
    try:
        item = Item.objects.get(pk=pk)
    except item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def index(request):
    return render(request, 'index.html', {})

def comandas(request):
    return render(request, 'comandas.html', ComandaListView.get_queryset() )

class ComandaListView(generic.ListView):
    model = Comanda
    context_object_name = 'comanda_list'
    queryset = model.objects.exclude(status='Paga')
    template_name = "../templates/comandas.html"

class ComandaDetailView(generic.DetailView):
    model = Comanda
    
    def get_context_data(self, **kwargs):
        comanda = get_object_or_404(Comanda, pk=self.kwargs['pk'])
        comanda_itens = ComandaItens.objects.all().filter(comanda=comanda)
        context = super(ComandaDetailView, self).get_context_data(**kwargs)
        context['comanda'] = comanda
        context['comanda_itens'] = comanda_itens
        return context


class ComandaPagarView(generic.DetailView):
    model = Comanda

    def get(self, request, pk):
        comanda = get_object_or_404(Comanda, pk=self.kwargs['pk'])
        comanda.pagarComanda()
        print("entrou")
        return render(request, 'comanda_paga.html')
        