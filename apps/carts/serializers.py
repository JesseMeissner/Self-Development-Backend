from .models import Carts
from rest_framework import serializers

class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Carts
        fields = ['quantity', 'item']
        depth = 1