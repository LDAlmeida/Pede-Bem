from django.contrib import admin
from .models import Usuario, Item, Pedidos

admin.site.register(Usuario)
admin.site.register(Item)
admin.site.register(Pedidos)