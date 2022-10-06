from pyexpat import model
from rest_framework import serializers

from .models import Comanda, ComandaItens


class ComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fields = '__all__'
        depth = 1
