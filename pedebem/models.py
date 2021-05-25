from djongo import models

class Item(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
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
    id = models.IntegerField(primary_key=True, unique=True)
    nome = models.TextField(max_length=30)
    cpf = models.TextField(max_length=11)
    role = models.CharField(max_length=30, choices = USER_CHOICES)
    login = models.TextField(max_length=30)
    senha = models.TextField(max_length=30)
    
    def __str__(self):
        return self.nome

class Comanda(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    mesa = models.IntegerField()
    items = models.ArrayField(model_container = Item,)
    atendente = models.EmbeddedField(model_container = Usuario)
    ativa = models.BooleanField()

    def __str__(self):
        return self.mesa
        
