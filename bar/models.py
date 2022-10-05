from pyexpat import model
from django.db import models
from django.urls import reverse

# Create your models here.

STATUS_COMANDA_CHOICES = [
    ('Aberta', 'Aberta'),
    ('Fechada', 'Fechada'),
    ('Paga', 'Paga')
]

class Mesa(models.Model):
    nome = models.TextField(max_length=20)

    def __str__(self) -> str:
        return self.nome

class Funcionario(models.Model):
    nome = models.TextField(max_length=56)

    def __str__(self) -> str:
        return self.nome

class Item(models.Model):
    nome = models.TextField(max_length=256)
    preco = models.IntegerField()

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name_plural = "Itens"

class Comanda(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    itens = models.ManyToManyField(Item, through='ComandaItens', verbose_name="Itens na comanda")
    total = models.IntegerField(blank=True, null=True)
    status = models.CharField(choices=STATUS_COMANDA_CHOICES, max_length=20, blank=True, null=True)

    def __str__(self) -> str:
        return "Comanda da mesa " + self.mesa.nome

    def save(self, *args, **kwargs):
        if not self.status:
            self.status = "Aberta"
        super().save(*args, **kwargs)

    def fecharComanda(self):
        queryset = ComandaItens.objects.filter(comanda=self)
        print(queryset)
        sum_valor = sum([item.item.preco * item.quantidade for item in queryset])
        print(sum_valor)
        self.total = sum_valor
        self.save(update_fields=["total"])

    def pagarComanda(self):
        self.status = "Paga"
        self.save()
    
class ComandaItens(models.Model):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.comanda.fecharComanda()

    def __str__(self) -> str:
        return self.item.nome

    class Meta:
        verbose_name_plural = "Comanda Itens"


class Bar(models.Model):
    comandas = models.ManyToManyField(Comanda, verbose_name="Comandas")


