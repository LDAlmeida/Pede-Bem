from django.db import models
from django.contrib.postgres.fields import ArrayField

class Item(models.Model):
    nome = models.TextField(max_length=30)
    descricao = models.TextField(max_length=256)
    valor = models.FloatField()

    def __str__(self):
        return self.nome

USER_CHOICES = {
    ("1", "Cliente"),
    ("2", "Atendente"),
    ("3", "Caixa"),
    ("4", "Gerente"),
}

class Usuario(models.Model):
    nome = models.TextField(max_length=30)
    cpf = models.TextField(max_length=11)
    role = models.CharField(max_length=30, choices = USER_CHOICES)
    login = models.TextField(max_length=30)
    senha = models.TextField(max_length=30)
    
    def __str__(self):
        return self.nome

PEDIDOS_CHOICES ={
    ("1", "Aguardando"),
    ("2", "Preparando"),
    ("3", "Pronto"),
    ("4", "Entregue")
}
class Pedidos(models.Model):
    mesa = models.IntegerField()
    item = models.ManyToManyField(Item)
    atendente = models.ManyToManyField(Usuario)
    status = models.CharField(max_length=30, choices=PEDIDOS_CHOICES)

    def __str__(self):
        return str(self.mesa) + " - " + str(self.item.all()) + " - " + str(self.status)
        