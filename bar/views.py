from django.shortcuts import render, get_object_or_404
from django.views import generic

from bar.models import Comanda, ComandaItens
# Create your views here.

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
        